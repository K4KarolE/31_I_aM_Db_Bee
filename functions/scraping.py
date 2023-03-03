from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

import pyperclip
import sys
import webbrowser

from functions import messages
from functions import settings              # from settings_db.json getting the info for the POSTER CHECKBOX, ROLDOWN MENU
                                            
def get_link():
    settings_data = settings.open_settings()    # opening the settings_db.json DB
    link = pyperclip.paste()
    counter = 0
    while 'imdb.com/title/' not in link:
        counter += 1
        messages.error_pop_up('wrong_link')
        link = pyperclip.paste()
        if counter == 2:
            messages.error_pop_up('bye_bye')
            settings_data['run_by_start'] = 0       # set the RUN BY START value to 0, so the next start the ENGINE will not be launched
            settings.save_settings(settings_data)
            sys.exit()
    return link

def web_driver():
    settings_data = settings.open_settings()
    link = get_link()
    # SET UP
    service = Service(executable_path= settings_data["path_chrome_driver"])
    options = Options()
    options.add_argument("window-size=1300,1400")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])      # disable the "DevTools listening on ws://127.0..." console message
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    # DRIVER
    driver = webdriver.Chrome(options=options, service=service) 
    # driver.minimize_window()
    driver.get(link)
    # print(user_agent)

#### DECIDER
    try:
        # Movies
        try:                                                
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                    By.CSS_SELECTOR, 'ul.ipc-inline-list:nth-child(2) > li:nth-child(1) > a:nth-child(1)'))
            )                       
            
            decider_read = driver.find_element(
            By.CSS_SELECTOR, 'ul.ipc-inline-list:nth-child(2) > li:nth-child(1) > a:nth-child(1)').text
        except:
              pass
        # Series
        try:                                                
            element = WebDriverWait(driver, 0).until(       # 0 = no wait <- the site should be already loaded in the previous section
            EC.presence_of_element_located((
                    By.CSS_SELECTOR, 'ul.ipc-inline-list:nth-child(2) > li:nth-child(1)'))
            )                       
            
            decider_read = driver.find_element(
            By.CSS_SELECTOR, 'ul.ipc-inline-list:nth-child(2) > li:nth-child(1)').text
        except:
              pass
              
    except:
        messages.message('error', 2, 'error_decider')
        driver.quit()
        sys.exit()

    decider = None
    if len(decider_read) == 4:        # 1992 - year -> Movie, Short Film
        decider = 'movie'
    if 'Series' in decider_read:      # TV Series, TV Mini Series
        decider = 'series'
    if decider == None:               # TV Movie, TV Special
        decider = 'tv_movie'

### MOVIE TITLE
    try:
        titleRead = driver.find_element(By.CSS_SELECTOR, '.sc-afe43def-1').text
    except:
        messages.message('error', 2, 'error_movie_title')
        driver.quit()
        sys.exit()

### YEAR OF RELEASE
    if decider == 'movie':
        index = 1
    else:
        index = 2  # series, tv_movie
    try:
        yearRead = driver.find_element(
        By.CSS_SELECTOR, f'ul.ipc-inline-list:nth-child(2) > li:nth-child({index}) > a:nth-child(1)').text
                    
    except:
            messages.message('error', 2, 'error_year')

### DIRECTOR(S)
    directors = []
    if decider in ['movie', 'tv_movie']:    # series do not have directors on the front page
        try:    
                for counter in range(1,4):
                        directors = directors +[driver.find_element(
                        By.CSS_SELECTOR, f'.sc-eda143c4-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({counter}) > a:nth-child(1)').text]
        except:
                pass # most of the time the movies have only 1 director -> would trigger an error message / not help to identify, if there is a valid error

### STAR(S)
    stars = []
    if decider in ['movie', 'tv_movie']:
        index_s = 3
    else:
        index_s = 2
    try:    
            for counter in range(1,4):
                    stars = stars + [driver.find_element(
                    By.CSS_SELECTOR, f'.sc-eda143c4-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child({index_s}) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({counter}) > a:nth-child(1)').text]
    except:
            messages.message('error', 2, 'error_stars') # would be triggered if the movie has less than 3 stars (not common)
            
### GENRE(S)
    genres= []
    try:    
            for counter in range(1,4):
                    genres = genres + [driver.find_element(
            By.CSS_SELECTOR, f'a.ipc-chip--on-baseAlt:nth-child({counter}) > span:nth-child(1)').text]

    except:
            pass # would be triggered if the movie has less than 3 genres

### LENGTH VALUE
    if decider == 'movie':  # format: 1992 15 1h 35m 
        index_l_1 = 3   
        # index_l_2 = 3     # UPDATE 03/03/23 - Test for a while
        
    else:                   # format: TV Series 2011–2019 18 57m
        index_l_1 = 4
        # index_l_2 = 4
    try:
        # taking the 2nd item(1h 33m) from "2022 1h 33m"
        movieLengthSum = driver.find_element(
        By.CSS_SELECTOR, f'ul.ipc-inline-list:nth-child(2) > li:nth-child({index_l_1})').text

        # # if the movie has classification(pg-13): "2022 pg-13 1h 33m" taking the 3rd item         # UPDATE 03/03/23 - Test for a while
        # if 'h' not in list(movieLengthSum) or 'm' not in list(movieLengthSum):
        #         movieLengthSum = driver.find_element(
        #         By.CSS_SELECTOR, f'.sc-f26752fb-0 > li:nth-child({index_l_2})').text
    except:
        movieLengthSum = None
        messages.message('error', 2, 'error_length')

### VALUATE AND TRANSFORM THE LENGTH VALUE(S)
    lengthHour = None
    lengthMinute = None
    # JUST ONE ITEM LENGTH VALUE, LIKE 45m OR 2h
    if len(str(movieLengthSum).split()) == 1:
            if 'h' in list(str(movieLengthSum)):
                    lengthHour = str(movieLengthSum).strip('hm')    # removing the "h" or "m" values, i know, in this scenario, just 'h' should be fine
            if 'm' in list(str(movieLengthSum)):
                    lengthMinute = str(movieLengthSum).strip('hm')

    # TWO ITEMS LENGTH VALUES, LIKE 2h 32m
    if len(str(movieLengthSum).split()) == 2:
            lengthList = str(movieLengthSum).split()
            lengthHour = lengthList[0].strip('hm')
            lengthMinute = lengthList[1].strip('hm')

### POSTER IMAGE
    if settings_data['poster_open_in_new_tab'] == 1:
        try:
            poster = driver.find_element(By.CSS_SELECTOR, '.ipc-media--poster-l > img:nth-child(1)')
            posterLink = poster.get_attribute('srcset')
            posterLink_list = posterLink.split() # making a list devided by the space(link(1st in the list) size, link(3rd) size, link(5th) size)
            
            selected_poster_size = settings_data['poster_size']     # Small, Medium...
            selected_poster_size_value = settings_data["poster_size_options"][selected_poster_size]     # 0 - Small, 2 - Medium, 4 - Larger

            if selected_poster_size != "All sizes":     # just open a specific size of poster
                webbrowser.open(posterLink_list[selected_poster_size_value])
            else:                                     # ALL SIZES     
                webbrowser.open(posterLink_list[0])   # small
                webbrowser.open(posterLink_list[2])   # medium
                webbrowser.open(posterLink_list[4])   # larger
        except:
                messages.message('error', 2, 'error_poster')
    
    driver.quit()

    return titleRead, yearRead, directors, stars, genres, lengthHour, lengthMinute