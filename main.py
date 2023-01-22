
from tkinter import *
from tkinter import filedialog      # target_sheet
import tkinter.messagebox           # for pop-up windows

from functions import settings
settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)

import engine

# STYLE
background_color = '#F0F0F0' # IMDb yellow: #E6B91E // default: #F0F0F0
font_style = 'Georgia'



window = Tk()
window.title('I am D bee - Window')
width = 500
length = 600
window.geometry(f'{width}x{length}')
window.configure(background=background_color)

checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'IMDb link in clipboard' ],     # [0/1, button, text]
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Autorun by next start' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ],
    'no_picture': ['no_picture_in_sheet', 'no_picture_in_sheet_button', 'No pictures in target sheet' ]
}


# TITLE - will be a picture
window_title = Label(window, text ='I am D bee',
height = 2,
font = (font_style, 20),
background=background_color)


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

filename = None
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

# CHROME DRIVER
chrome_driver_text = "Chrome driver path"
chrome_driver_field = Text(window, height = 1, width = 20)
chrome_driver_field.insert(END,settings_data["path_chrome_driver"])   # set to the latest saved PATH value
chrome_driver_field_title = Label(window, text = chrome_driver_text)
chrome_driver_field_title.config(font =(font_style, 12))

filename = None
def browseSheet_3():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Executable", "*.exe"),
                        ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    chrome_driver_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    chrome_driver_field.insert(END,filename)     # adding the path and the name of the selected file

chrome_driver_button = Button(window,
text = ">>",
command = browseSheet_3)


## POSTER SIZE - ROLL DOWN MENU
poster_size_options = []
for item in settings_data['poster_size_options'].keys():        # creating a list of the POSTER SIZE OPTIONS holded in settings_db.json / poster_size_options
    poster_size_options = poster_size_options + [item]

clicked = StringVar()
clicked.set(settings_data['poster_size'])       # # set to the latest saved value
poster_roll_down = OptionMenu( window, clicked, *poster_size_options )


### SAVE SETTINGS, START THE ENGINE
def save_and_start():
    # CLIPBOARD CHECKBOX
    settings_data['imdb_link_in_clipboard'] = checkbox['clipboard'][0].get()
    
    # POSTER IN NEW TAB - CHECKBOX + ROLL DOWN BUTTON
    settings_data['poster_open_in_new_tab'] = checkbox['poster'][0].get() 
    settings_data['poster_size'] = clicked.get()

    # RUN BY START CHECKBOX
    settings_data['run_by_start'] = checkbox['run'][0].get()

    # NO PICTURE IN TARHET SHEET CHECKBOX
    settings_data['no_picture_in_sheet'] = checkbox['no_picture'][0].get()

    # LOOK FOR NATIVE TITLE - CHECKBOX + ROLL DOWN BUTTON
    settings_data['title_search'] = checkbox['title'][0].get()                      # from CHECKBOXES for loop: variable = item[0] -> item[0] = checkbox['title'][0]
    settings_data['title_search_link_selected'] = title_search_clicked.get()        # Hungarian / Czech..

    # CHROME DRIVER PATH FIELD
    settings_data['path_chrome_driver'] = chrome_driver_field.get("1.0", "end-1c")

    # TARGET SHEET PATH FIELD
    settings_data['path_movie_new_record'] = target_sheet_field.get("1.0", "end-1c")

    # MOVIES DB SHEET PATH FIELD
    settings_data['path_movies_db_sheet'] = movies_db_sheet_field.get("1.0", "end-1c")

    settings.save_settings(settings_data)

    ### START ###
    ## MANDATORY FIELDS CHECK   
    error_popup_window_title = [
        'Got stuck in honey',
        'Danger Will Robinson, danger!'
        ]
    # CHROME DRIVER
    if chrome_driver_field.get("1.0", "end-1c") == '':
        tkinter.messagebox.showinfo(error_popup_window_title[1], f"#{chrome_driver_text}# needs to be added")   # error pop-up message
        return
    # TARGET SHEET
    if target_sheet_field.get("1.0", "end-1c") == '':
        tkinter.messagebox.showinfo(error_popup_window_title[1], f"#{target_sheet_text}# needs to be added")   # error pop-up message
        return
    # NO PICTURES IN TARGET SHEET - CHECKBOX
    if checkbox['no_picture'][0].get() == 0:
        tkinter.messagebox.showinfo(error_popup_window_title[1], f"#{checkbox['no_picture'][2]}# checkbox is not selected")   # error pop-up message
        return
    # IMDb LINK IN CLIPBOARD - CHECKBOX
    if checkbox['clipboard'][0].get() == 0:
        tkinter.messagebox.showinfo(error_popup_window_title[1], f"#{checkbox['clipboard'][2]}# checkbox is not selected\n\nClick OK once the link is copied")   # error pop-up message
    
    engine.start_engine()   # will start data collection / save to excel sheet / if selected: open poster and native title search in new tabs, open movie DB sheet...
    

button_save_and_start = Button(window,
text = "Start",
command = save_and_start,       # no () otherwise will execute it before clicking the button 
font = (font_style, 15))        # binding multiple commands to the same button: command = lambda: [save_settings(), engine.start_engine()]


### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    # X
    display_x = 140
    display_x_button_gap = 170
    # Y
    display_y_BASE = 80
    display_y_GAP = 30

    def y_location(gap_by_number):
        display_y = display_y_BASE + display_y_GAP * gap_by_number
        return display_y


    # WINDOW TITLE
    window_title.place(x=display_x+40, y=10)

    # CLIPBOARD CHECKBOX
    checkbox['clipboard'][1].place(x=display_x, y=y_location(0))

    # POSTER CHECKBOX + ROLL DOWN BUTTON
    checkbox['poster'][1].place(x=display_x, y=y_location(1))
    poster_roll_down.place(x=display_x+display_x_button_gap, y=y_location(1) + 7)

    # LOOK FOR NATIVE TITLE + ROLL DOWN BUTTON
    checkbox['title'][1].place(x=display_x, y=y_location(2))
    title_search_roll_down.place(x=display_x+display_x_button_gap, y=y_location(2) + 7)

     # RAUN BY START CHECKBOX
    checkbox['run'][1].place(x=display_x, y=y_location(3))

    # CHROME DRIVER PATH - TITEL + FIELD + BUTTON
    chrome_driver_field_title.place(x=display_x, y=y_location(5))
    chrome_driver_field.place(x=display_x+3, y=y_location(5)+25)
    chrome_driver_button.place(x=display_x+display_x_button_gap, y=y_location(5)+13)

    # TARGET SHEET PATH - TITEL + FIELD + BUTTON
    target_sheet_field_title.place(x=display_x, y=y_location(7))
    target_sheet_field.place(x=display_x+3, y=y_location(7)+25)
    target_sheet_button.place(x=display_x+display_x_button_gap, y=y_location(7)+13)

    # NO PICTURE IN TARHET SHEET CHECKBOX
    checkbox['no_picture'][1].place(x=display_x, y=y_location(8)+10)

    # MOVIES DB SHEET PATH - TITEL + FIELD + BUTTON
    movies_db_sheet_field_title.place(x=display_x, y=y_location(10))
    movies_db_sheet_field.place(x=display_x+3, y=y_location(10)+25)
    movies_db_sheet_button.place(x=display_x+display_x_button_gap, y=y_location(10)+13)

    # SAVE SETTINGS BUTTON
    button_save_and_start.place(x=display_x+50, y=y_location(12)+10)

display_widgets()

## START THE ENGINE AUTOMATICALLY WHEN THE run by start CHECKBOX VALUE SAVED AS 1/checked
# if settings_data['run_by_start'] == 1:
#     engine.start_engine()


window.mainloop()