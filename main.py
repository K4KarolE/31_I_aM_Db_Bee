'''
test 2
- should be able to select automatically the callable script/scenario: Movie - Series - TV
- link from clipboard
- how to pass the link from main to the called script?
- buttons: get link, start, requirements, help, excel temp downloadable?, contact(email)
- field where able to select the excel file and location?
    + file name valuation, if not using the excel sheet provided -> warning message?
    + able to save as default?
- unique window icon? (top left)
- able to amend the frame?
- error messages pop-up?
- bee waving animation? hand and eyebrow? (looping images?)

- looking for hungarian title? switchable button? clever how to pass to the called script?

Requirements:
- Python
- Selenium Webdriver
- pop-up for first time users? how to tell first time user?

'''

from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.imdb.com/title/tt0104952/?ref_=nv_sr_srsg_0').text  #Movie - 1 director
html_text = requests.get('https://www.imdb.com/title/tt0120855/?ref_=nv_sr_srsg_0').text  #Movie - 2 Directors
# html_text = requests.get('https://www.imdb.com/title/tt0944947/?ref_=nv_sr_srsg_0').text  #TV Show
# html_text = requests.get('https://www.imdb.com/title/tt15318872/?ref_=adv_li_tt').text  #TV Special
soup = BeautifulSoup(html_text, 'lxml')

title = soup.find(class_='sc-b73cd867-0 eKrKux').text
year = soup.find(class_='sc-8c396aa2-2 itZqyK').text
directors = soup.find(class_='sc-fa02f843-0 fjLeDR')
director_first = directors.find('li', class_='ipc-inline-list__item').text


print()
print(f"{title} - {year}\n")
print(director_first + '\n')




