'''

worked fine just got blocked = "403 Forbidden"

adding headers did not help

lesson learned

'''

from bs4 import BeautifulSoup
import requests


## Data Scraping ##
headers = { 'User Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'}

html_text = requests.get('https://www.imdb.com/title/tt0104952/?ref_=nv_sr_srsg_0', headers=headers).text   #Movie - 1 director
# html_text = requests.get('https://www.imdb.com/title/tt0120855/?ref_=nv_sr_srsg_0').text                  #Movie - 2 Directors
# html_text = requests.get('https://www.imdb.com/title/tt0944947/?ref_=nv_sr_srsg_0').text                  #TV Show
# html_text = requests.get('https://www.imdb.com/title/tt15318872/?ref_=adv_li_tt').text                    #TV Special

soup = BeautifulSoup(html_text, 'lxml')

# Title
title = soup.find(class_='sc-b73cd867-0 eKrKux').text

# Year
year = soup.find(class_='sc-8c396aa2-2 itZqyK').text

# Directors - Actors
crew_content = soup.find(class_='sc-fa02f843-0 fjLeDR')
crew_tag = crew_content.find_all('div')

i_counter = 0
directors = []
actors = []

if soup.find(class_='sc-89e7233a-1 dWZpw episode-guide-text'):  # TV Show - Episode guide section - only in shows/series
    for i in crew_tag:       
        i_counter += 1      
        for k in i:
            for t in k:
                if i_counter == 2:                              # directors are not displayed on the main page for TV Shows
                    actors = actors + [t.a.text]                # taking just the actors` values

else:                                                           # Movie / TV Special
    for i in crew_tag:       
        i_counter += 1      
        for k in i:
            for t in k:
                if i_counter == 1:
                    directors = directors + [t.a.text]
                if i_counter == 3:
                    actors = actors + [t.a.text]

# Genre
genre_content = soup.find(class_='ipc-chip-list--baseAlt ipc-chip-list sc-16ede01-5 ggbGKe')
genre_tag = genre_content.find_all('a')
genres = []
for i in genre_tag:
    genres = genres + [i.text]

# Poster
poster_content = soup.find('div', class_='ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-d383958-0 gvOdLN celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2')
poster_link = poster_content.find('img', src=True)
# poster_link['src']

print()
print(f'{title} - {year}')
print()
print(genres)
print()
print(directors)
print()
print(actors)
print()
print(poster_link['src'])