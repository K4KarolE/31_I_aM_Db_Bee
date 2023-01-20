
from tkinter import *
from tkinter import filedialog      # target_sheet
import tkinter.messagebox           # for pop-up windows
from functions import settings

font_style = 'Georgia'
filename = None

settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)

window = Tk()
window.title('I am D bee - Window')
width = 500
length = 600
window.geometry(f'{width}x{length}')

checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'IMDb Link in clipboard' ],
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Run by start' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ]
}


# TITLE - will be a picture
window_title = Label(window, text ='I am D bee',
height = 2,
font = (font_style, 20))


# CHECKBOXES
for item in checkbox.values():
    first_list_item = item[0]                               # we need the titles of first items in the dic. values('imdb_link_in_clipboard'..) in the next line
    item[0] = IntVar(value=settings_data[first_list_item])  # loading the previosly saved values (ticked/unticked) from settings_db.json
    item[1] = Checkbutton(
        window,
        text = item[2],
        variable = item[0], 
        height = 2,
        font = (font_style, 12)
        )


# TITLE SEARCH - BUTTON
title_search_options = []
for item in settings_data['title_search_links'].keys():
    title_search_options = title_search_options + [item]    # creating a list of the "title_search_links" dictonary`s keys (Hungarian / Czech /..) from settings_db.json
                                                            # adding new title link key-value pair: just add it to the settings_db.json / "title_search_links" dictionary
title_search_clicked = StringVar()
title_search_clicked.set(settings_data['title_search_link_selected'])   # set to the latest saved value (Hungarian / Czech /..)
title_search_roll_down = OptionMenu( window, title_search_clicked, *title_search_options )


## PATH FIELDS - SEARCHBOXES
# TARGET SHEET
target_sheet_text = "Target sheet path"
target_sheet_field = Text(window, height = 1, width = 20)
target_sheet_field.insert(END,settings_data['path_movie_new_record'])   # set to the latest saved PATH value
target_sheet_field_title = Label(window, text = target_sheet_text)
target_sheet_field_title.config(font =(font_style, 12))

def browseSheet_1():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                        ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    target_sheet_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    target_sheet_field.insert(END,filename)     # adding the path and the name of the selected file

target_sheet_button = Button(window,
text = ">>",
command = browseSheet_1)

# MOVIES DB SHEET
movies_db_sheet_field = Text(window, height = 1, width = 20)
movies_db_sheet_field.insert(END,settings_data['path_movies_db_sheet'])    # set to the latest saved PATH value
movies_db_sheet_field_title = Label(window, text = "Movies DB sheet path")
movies_db_sheet_field_title.config(font =(font_style, 12))

def browseSheet_2():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                        ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    movies_db_sheet_field.delete('1.0', END)        # once a button is clicked, removes the previous value
    movies_db_sheet_field.insert(END,filename)      # adding the path and the name of the selected file

movies_db_sheet_button = Button(window,
text = ">>",
command = browseSheet_2)


## POSTER SIZE - ROLL DOWN MENU
poster_size_options = [
"Small",
"Medium",
"Larger",
"All sizes"
]

clicked = StringVar()
clicked.set(settings_data['poster_size'])       # # set to the latest saved value
poster_roll_down = OptionMenu( window, clicked, *poster_size_options )


### SAVE SETTINGS
def save():
    # CLIPBOARD CHECKBOX
    settings_data['imdb_link_in_clipboard'] = checkbox['clipboard'][0].get()
    
    # POSTER IN NEW TAB - CHECKBOX + ROLL DOWN BUTTON
    settings_data['poster_open_in_new_tab'] = checkbox['poster'][0].get() 
    settings_data['poster_size'] = clicked.get()

    # RUN BY START CHECKBOX
    settings_data['run_by_start'] = checkbox['run'][0].get()

    # LOOK FOR NATIVE TITLE - CHECKBOX + ROLL DOWN BUTTON
    settings_data['title_search'] = checkbox['title'][0].get()                      # from CHECKBOXES for loop: variable = item[0] -> item[0] = checkbox['title'][0]
    settings_data['title_search_link_selected'] = title_search_clicked.get()        # Hungarian / Czech..

    # TARGET SHEET PATH FIELD
    settings_data['path_movie_new_record'] = target_sheet_field.get("1.0", "end-1c")

    # MOVIES DB SHEET PATH FIELD
    settings_data['path_movies_db_sheet'] = movies_db_sheet_field.get("1.0", "end-1c")

    settings.save_settings(settings_data)
button_save_settings = Button(window,
text = "Save settings",
command = save)

### START
def start():
    # MANDATORY FIELDS CHECK
    error_popup_window_title = ['Got stuck in honey','Danger Will Robinson, danger!']
    if checkbox['clipboard'][0].get() == 0:
        tkinter.messagebox.showinfo(error_popup_window_title[0], f"The #{checkbox['clipboard'][2]}# checkbox needs to be selected")     # error pop-up message

    if target_sheet_field.get("1.0", "end-1c") == '':
        tkinter.messagebox.showinfo(error_popup_window_title[0], f"The #{target_sheet_text}# needs to be added")        # error pop-up message



button_start = Button(window,
text = "START",
command = start)


### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    display_x = 140
    display_x_button_gap = 170
    # display_y_base = 80
    # displaey_y_gap = 30

    # WINDOW TITLE
    window_title.place(x=display_x+40, y=10)

    # CLIPBOARD CHECKBOX
    checkbox['clipboard'][1].place(x=display_x, y=80)

    # POSTER CHECKBOX + ROLL DOWN BUTTON
    checkbox['poster'][1].place(x=display_x, y=110)
    poster_roll_down.place(x=display_x+display_x_button_gap, y=115)

    # RAUN BY START CHECKBOX
    checkbox['run'][1].place(x=display_x, y=140)

    # LOOK FOR NATIVE TITLE + ROLL DOWN BUTTON
    checkbox['title'][1].place(x=display_x, y=170)
    title_search_roll_down.place(x=display_x+display_x_button_gap, y=175)

    # TARGET SHEET PATH TITEL + FIELD + target_sheet BUTTON
    target_sheet_field_title.place(x=display_x, y=230)
    target_sheet_field.place(x=display_x, y=250)
    target_sheet_button.place(x=display_x+display_x_button_gap, y=243)

    # MOVIES DB SHEET PATH TITEL + FIELD + target_sheet BUTTON
    movies_db_sheet_field_title.place(x=display_x, y=280)
    movies_db_sheet_field.place(x=display_x, y=300)
    movies_db_sheet_button.place(x=display_x+display_x_button_gap, y=293)

    # SAVE SETTINGS BUTTON
    button_save_settings.place(x=display_x+50, y=350)

    # START BUTTON
    button_start.place(x=display_x+65, y=400)
display_widgets()



window.mainloop()