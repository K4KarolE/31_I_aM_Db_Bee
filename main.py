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
- bs4
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

# Director(s) - Actor(s)
director_actor = soup.find(class_='sc-fa02f843-0 fjLeDR')
section = director_actor.find_all('div')

i_counter = 0
directors = []
actors = []
for i in section:       # in 3 divesion we looking for the 1st(director) and 3rd(actor)
    i_counter += 1      # names, with no extra info like: (directed by), (voice)
    for k in i:
        for t in k:
            if i_counter == 1:
                directors = directors + [t.a.text]
            if i_counter == 3:
                actors = actors + [t.a.text]

print(directors)
print()
print(actors)


# directors = director_ul.find_all('li')
# directors_list = []
# for i in directors:
#     directors_list = directors_list + [i.text]

# actor_ul = director_actor.find('div', class_='ipc-metadata-list-item__content-container')
# actors = actor_ul.find_all('li')
# actors_list = []
# for i in actors:
#     actors_list = actors_list + [i.text]


# print()
# print(f"{title} - {year}\n")
# print('Director(s):')
# for i in directors_list:
#     print(f"{i} ")

# print()

# for i in actors_list:
#     print(f"{i} ")





