
from tkinter import *
from tkinter import filedialog      # searchbox

font_style = 'Georgia'
filename = None

window = Tk()
window.title('I am D bee - Window')
window.geometry('600x800')

# TITLE - will be a picture
w = Label(window, text ='I am D bee',
height = 2,
font = (font_style, 20))
w.pack()

checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'Link in clipboard' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ],
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Run by start' ]
}

searchbox = {
    'movie_new_record': ['imdb_link_in_clipboard', 'clipboard_button', 'Path to the target sheet' ],
    'movies_sheet': ['title_search', 'title_search_button', 'Path to your movie database sheet' ],

}

# CHECKBOXES
for item in checkbox.values():
    item[0] = IntVar()
    item[1] = Checkbutton(
        window,
        text = item[2],
        variable = item[0], 
        height = 2,
        font = (font_style, 12)
        )
    item[1].pack()

## FIELD FOR SEARCHBOX

searchBox_field = Text(window, height = 1, width = 50)

searchBox_field_title = Label(window, text = "Your target sheet path")
searchBox_field_title.config(font =(font_style, 12))

searchBox_field_title.pack()
searchBox_field.pack()

## SEARCHBOXES
def browseSheet_1():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                           ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    searchBox_field.delete('1.0', END)
    searchBox_field.insert(END,filename)

button_explore = Button(window,
text = "Browse Files",
command = browseSheet_1)


button_explore.pack()






window.mainloop()

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