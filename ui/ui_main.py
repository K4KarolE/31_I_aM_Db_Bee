
from tkinter import *

font_style = 'Georgia'

root = Tk()
root.title('I am D bee')
root.geometry('450x600')

# TITLE - will be a picture
w = Label(root, text ='I am D bee',
height = 2,
font = (font_style, 20))
w.pack()



checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'Link in clipboard' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ],
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Run by start' ]
}

for item in checkbox.values():
    item[0] = IntVar()
    item[1] = Checkbutton(root, text = item[2],
    variable = item[0], 
    height = 2,
    font = (font_style, 12))
    item[1].pack()




root.mainloop()


'''
Information from the user

checkbox: 4
searchbox: 2
field: 1
rolldown: 1

checkbox     "imdb_link_in_clipboard": true,     mandatory
searchbox    "path_movies_sheet": "",
searchbox    "path_movie_new_record": "",        mandatory
checkbox     "title_search": true,
field        "title_search_link": "",            if "title_search": true - mandatory // roll down menu? greyed out otherwise? - able to add new link?
checkbox     "poster_open_in_new_tab": true,
rolldown     "poster_size": "",                  small by default / medium / larger // greyed out otherwise?
checkbox     "run_by_start": false

button - save current settings - message: will load automatically with next start

'''