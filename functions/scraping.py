#!/bin python3.11

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyperclip

from datetime import date
import sys
import webbrowser
import platform

import messages

def get_link():
    link = pyperclip.paste()
    if 'www.imdb.com/title/' not in link:
        messages.link_error()
        sys.exit()
    return link


def web_driver():
    link = get_link()
    if platform.system() == 'Windows':
        service = Service('C:\Program Files (x86)\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.minimize_window()
        driver.get(link)

    if platform.system() == 'Linux':
        service = Service('/home/zsandark/_DEV/Support/Chrome_driver/chromedriver')
        driver = webdriver.Chrome(service=service)
        # driver.minimize_window()
        driver.get(link)

#### DECIDER
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
                By.CSS_SELECTOR, '.sc-8c396aa2-0 > li:nth-child(1)'))
        )                       
        
        decider_read = driver.find_element(
        By.CSS_SELECTOR, '.sc-8c396aa2-0 > li:nth-child(1)').text      
    except:
            print()
            print('*** ERROR - DECIDER ***')
            print()
            driver.quit()
            sys.exit()
    
    # print(decider_read)

    decider = None
    if len(decider_read) == 4:        # 1992 - year -> Movie, Short Film
        decider = 'movie'
    if 'Series' in decider_read:      # TV Series, TV Mini Series
        decider = 'series'
    if decider == None:               # TV Movie, TV Special
        decider = 'tv_movie'

    
### MOVIE TITLE - SAME FOR ALL 3 DECIDER CATEGORIES
    try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                    By.CSS_SELECTOR, '.sc-b73cd867-0'))
            )                       
            
            titleRead = driver.find_element(
            By.CSS_SELECTOR, '.sc-b73cd867-0').text
    except:
            print()
            print('*** ERROR - MOVIE TITLE ***')
            print()
            driver.quit()
            sys.exit()

### YEAR OF RELEASE
    if decider == 'movie':
        index = 1
    else:
        index = 2  # series, tv_movie
    try:
        yearRead = driver.find_element(
        By.CSS_SELECTOR, f'.sc-8c396aa2-0 > li:nth-child({index}) > a:nth-child(1)').text
                    
    except:
            print()
            print('*** ERROR - YEAR OF RELEASE ***')
            print()

### DIRECTOR(S) - SAME AS MOVIE
    directors = []
    if decider in ['movie', 'tv_movie']:    # series do not have directors on the front page
        try:    
                for counter in range(1,4):
                        directors = directors +[driver.find_element(
                        By.CSS_SELECTOR, f'.sc-fa02f843-0 > ul:nth-child(1) > li:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({counter}) > a:nth-child(1)').text]
        except:
                pass # most of the time the movies have only 1 director -> would trigger an error message / not help to identify, if there is a valid error


    print(titleRead)
    print(yearRead)



get_link()
web_driver()






