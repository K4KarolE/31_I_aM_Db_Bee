from tkinter import *
from tkinter import filedialog      # for browse window (adding path)
import tkinter.messagebox           # for pop-up windows

import platform                     # to check which OS is used
import os
from pathlib import Path

import engine
from functions import settings
settings_data = settings.open_settings()        # access to the saved/default settings (settings_db.json)


# COLORS - FONT STYLE
# IMDb yellow: #E6B91E // original tkinter grey: #F0F0F0 - FYI
skin_selected = settings_data['skin_selected']                                  # example: default
background_color = settings_data['skins'][skin_selected]['background_color']    # example: skins / default / background_color / #E6B91E
field_background_color = settings_data['skins'][skin_selected]['field_background_color'] 
font_style = settings_data['skins'][skin_selected]['font_style']
font_color = settings_data['skins'][skin_selected]['font_color']

# WINDOW
window = Tk()
window.title(settings_data['skins'][skin_selected]['window_title'])
width = 500
length = 600
window.geometry(f'{width}x{length}')
window.resizable(0,0)   # locks the main window
# window.configure(background="black")  - FYI

# IMAGES
working_directory = os.path.dirname(__file__)     # os.path.dirname(__file__) = D:\_DEV\Python\31_I_aM_D_bee   //in my case
path_image = Path(working_directory, "skins", skin_selected, "BG.png")      # Path functions makes the path OS independent, running the program on Windows: ..skins\default.., on Linux: ..skins/default..)
backgound_image = PhotoImage(file = path_image)
backgound_image_label = Label( window, image = backgound_image)
backgound_image_label.place(x = -2, y = 0)

if platform.system() == 'Windows':      # will not be visible on Linux, macOS
    path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
    window.iconbitmap(path_icon)        # window icon - left, top corner

## CHECKBOXES
checkbox = {
    'clipboard': ['imdb_link_in_clipboard', 'clipboard_button', 'IMDb link in clipboard' ],     # [0/1, button, text]
    'poster': ['poster_open_in_new_tab', 'poster_open_in_new_tab_button', 'Poster in a new tab' ],
    'run': ['run_by_start', 'run_by_start_button', 'Autorun by next start' ],
    'title': ['title_search', 'title_search_button', 'Look for native title' ],
    'no_picture': ['no_picture_in_sheet', 'no_picture_in_sheet_button', 'No pictures in sheet' ]
}

for item in checkbox.values():
    first_list_item = item[0]                               # we need the titles of first items in the dic. values('imdb_link_in_clipboard'..) in the next line
    item[0] = IntVar(value=settings_data[first_list_item])  # loading the previosly saved values (ticked/unticked) from settings_db.json
    item[1] = Checkbutton(
        window,
        text = item[2],
        variable = item[0], 
        height = 1,
        font = (font_style, 12),
        foreground=font_color,
        background=background_color,
        activeforeground = font_color,
        activebackground=background_color,   # activebackground - color when clicked
        highlightbackground=background_color
        )
checkbox['no_picture'][1].config(font = (font_style, 9))    # make the /No pictures in target sheet/ checkbox text smaller


## ROLL DOWN MENUS
# SKIN - ROLL DOWN MENU
# highlightbackground - color around the button
# activebackground - color when mouse over or clicked
def change_skin(__):
    settings_data['skin_selected'] = skins_roll_down_clicked.get()  # updating & saving the "skin_selected" value in settings_db.json with every click/skin change
    settings.save_settings(settings_data)
    skin_selected = skins_roll_down_clicked.get()

    # LIST OF WIDGETS TO UPDATE
    #TEXT
    window.title(settings_data['skins'][skin_selected]['window_title'])

    #IMAGES
    path_image = Path(working_directory, "skins", skin_selected, "BG.png")
    backgound_image.configure(file = path_image)

    if platform.system() == 'Windows': 
        path_icon = Path(working_directory, "skins", skin_selected, "icon.ico")
        window.iconbitmap(path_icon)

    ##COLORS
    background_color = settings_data['skins'][skin_selected]['background_color']
    font_color = settings_data['skins'][skin_selected]['font_color']
    
    # CHECKBOXES
    for item in checkbox.values():
        item[1].configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
    
    # ROLL DOWN MENUS
    skins_roll_down.configure(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    skins_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=background_color, activeforeground = "white")

    title_search_roll_down.configure(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    title_search_roll_down['menu'].configure(foreground=font_color, background=background_color, activeforeground = "white", activebackground=background_color)

    poster_roll_down.config(foreground=font_color, background=background_color, activeforeground=font_color, activebackground=background_color, highlightbackground=background_color)
    poster_roll_down["menu"].config(foreground=font_color, background=background_color, activeforeground = "white", activebackground=background_color)

    # PATH - FIELDS + SEARCHBOXES
    target_sheet_field.configure(foreground=font_color, background=background_color)
    target_sheet_field_title.configure(foreground=font_color, background=background_color)
    target_sheet_button.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

    movies_db_sheet_field.configure(foreground=font_color, background=background_color)
    movies_db_sheet_field_title.configure(foreground=font_color, background=background_color)
    movies_db_sheet_button.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

    chrome_driver_field.configure(foreground=font_color, background=background_color)
    chrome_driver_field_title.configure(foreground=font_color, background=background_color)
    chrome_driver_button.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

    # SAVE AND START BUTTON
    button_save_and_start.configure(foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

skins_options = []
for item in settings_data['skins'].keys():        # creating a list of the SKINS from settings_db.json / skins
    skins_options = skins_options + [item]

skins_roll_down_clicked = StringVar()
skins_roll_down_clicked.set("Skins")    
skins_roll_down = OptionMenu( window, skins_roll_down_clicked, *skins_options, command=change_skin)     
skins_roll_down.configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
skins_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=background_color)

# TITLE SEARCH - ROLL DOWN MENU
title_search_options = []
for item in settings_data['title_search_links'].keys():
    title_search_options = title_search_options + [item]    # creating a list of the "title_search_links" dictonary`s keys (Hungarian / Czech /..) from settings_db.json
                                                            # adding new title link key-value pair: just add it to the settings_db.json / "title_search_links" dictionary
title_search_roll_down_clicked = StringVar()
title_search_roll_down_clicked.set(settings_data['title_search_link_selected'])   # set to the latest saved value (Hungarian / Czech /..)
title_search_roll_down = OptionMenu( window, title_search_roll_down_clicked, *title_search_options )
title_search_roll_down.configure(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
title_search_roll_down['menu'].configure(foreground=font_color, background=background_color, activebackground=background_color)

# POSTER SIZE - ROLL DOWN MENU
poster_size_options = []
for item in settings_data['poster_size_options'].keys():        # creating a list of the POSTER SIZE OPTIONS holded in settings_db.json / poster_size_options
    poster_size_options = poster_size_options + [item]

poster_roll_down_clicked = StringVar()
poster_roll_down_clicked.set(settings_data['poster_size'])       # # set to the latest saved value
poster_roll_down = OptionMenu( window, poster_roll_down_clicked, *poster_size_options)
poster_roll_down.config(foreground=font_color, background=background_color, activeforeground = font_color, activebackground=background_color, highlightbackground=background_color)
poster_roll_down["menu"].config(foreground=font_color, background=background_color, activebackground=background_color)


## PATH - FIELDS + SEARCHBOXES
# TARGET SHEET - FIELD + SEARCHBOX
target_sheet_text = "Target sheet path"
target_sheet_field = Text(window, height = 1, width = 20, foreground=font_color, background=field_background_color)
target_sheet_field.insert(END,settings_data['path_movie_new_record'])   # set to the latest saved PATH value
target_sheet_field_title = Label(window, text = target_sheet_text, foreground=font_color, background=background_color)
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
target_sheet_button = Button(window, text = ">>", command = browseSheet_1, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

# MOVIES DB SHEET - FIELD + SEARCHBOX
movies_db_sheet_field = Text(window, height = 1, width = 20, foreground=font_color, background=field_background_color)
movies_db_sheet_field.insert(END,settings_data['path_movies_db_sheet'])    # set to the latest saved PATH value
movies_db_sheet_field_title = Label(window, text = "Movies DB sheet path", foreground=font_color, background=background_color)
movies_db_sheet_field_title.config(font =(font_style, 12))

def browseSheet_2():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                        ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    movies_db_sheet_field.delete('1.0', END)        # once a button is clicked, removes the previous value
    movies_db_sheet_field.insert(END,filename)      # adding the path and the name of the selected file
movies_db_sheet_button = Button(window, text = ">>", command = browseSheet_2, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)

# CHROME DRIVER - FIELD + SEARCHBOX
chrome_driver_text = "Chrome driver path"
chrome_driver_field = Text(window, height = 1, width = 20, foreground=font_color, background=field_background_color)
chrome_driver_field.insert(END,settings_data["path_chrome_driver"])   # set to the latest saved PATH value
chrome_driver_field_title = Label(window, text = chrome_driver_text, foreground=font_color, background=background_color)
chrome_driver_field_title.config(font =(font_style, 12))

def browseSheet_3():
    filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Executable", "*.exe"),
                        ("all files", "*.*")))
    # label_file_explorer.configure(text=filename)
    chrome_driver_field.delete('1.0', END)       # once a button is clicked, removes the previous value
    chrome_driver_field.insert(END,filename)     # adding the path and the name of the selected file
chrome_driver_button = Button(window, text = ">>", command = browseSheet_3, foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)


### BUTTONS
# SAVE SETTINGS, START THE ENGINE - BUTTON
def save_and_start():
    ## SETUP AND SAVE
    # CLIPBOARD CHECKBOX
    settings_data['imdb_link_in_clipboard'] = checkbox['clipboard'][0].get()
    
    # POSTER IN NEW TAB - CHECKBOX + ROLL DOWN BUTTON
    settings_data['poster_open_in_new_tab'] = checkbox['poster'][0].get() 
    settings_data['poster_size'] = poster_roll_down_clicked.get()

    # RUN BY START CHECKBOX
    settings_data['run_by_start'] = checkbox['run'][0].get()

    # NO PICTURE IN TARHET SHEET CHECKBOX
    settings_data['no_picture_in_sheet'] = checkbox['no_picture'][0].get()

    # LOOK FOR NATIVE TITLE - CHECKBOX + ROLL DOWN BUTTON
    settings_data['title_search'] = checkbox['title'][0].get()                              # from CHECKBOXES for loop: variable = item[0] -> item[0] = checkbox['title'][0]
    settings_data['title_search_link_selected'] = title_search_roll_down_clicked.get()      # Hungarian / Czech..

    # CHROME DRIVER PATH FIELD
    settings_data['path_chrome_driver'] = chrome_driver_field.get("1.0", "end-1c")

    # TARGET SHEET PATH FIELD
    settings_data['path_movie_new_record'] = target_sheet_field.get("1.0", "end-1c")

    # MOVIES DB SHEET PATH FIELD
    settings_data['path_movies_db_sheet'] = movies_db_sheet_field.get("1.0", "end-1c")

    # SKINS ROLL DOWN BUTTON
    # the skin is saved, when it is updated -> next time will load the latest used skin, without the need of the Save & Start button/process  

    settings.save_settings(settings_data)

    
    ### START ###
    ## MANDATORY FIELDS CHECK   
    error_popup_window_title = settings_data['skins'][skin_selected]['error_window_title']  # after skin switch the window title will be updated once the prog. restarted
    # CHROME DRIVER
    if chrome_driver_field.get("1.0", "end-1c") == '':
        tkinter.messagebox.showinfo(error_popup_window_title, f"#{chrome_driver_text}# needs to be added")   # error pop-up message
        return      # stops the function without exiting from the main script
    # TARGET SHEET
    if target_sheet_field.get("1.0", "end-1c") == '':
        tkinter.messagebox.showinfo(error_popup_window_title, f"#{target_sheet_text}# needs to be added")   # error pop-up message
        return
    # NO PICTURES IN TARGET SHEET - CHECKBOX
    if checkbox['no_picture'][0].get() == 0:
        tkinter.messagebox.showinfo(error_popup_window_title, f"#{checkbox['no_picture'][2]}# checkbox is not selected")   # error pop-up message
        return
    # IMDb LINK IN CLIPBOARD - CHECKBOX
    if checkbox['clipboard'][0].get() == 0:
        tkinter.messagebox.showinfo(error_popup_window_title, f"#{checkbox['clipboard'][2]}# checkbox is not selected\n\nClick OK once the link is copied")
        # error pop-up message, more relevant for the first time users
    engine.start_engine()   # will start data collection / save to excel sheet / if selected: open poster and native title search in new tabs, open movie DB sheet...
    
button_save_and_start = Button(window, text = "Save & Start", command = save_and_start, font = (font_style, 15), foreground=font_color, background=background_color, activeforeground=background_color, activebackground=font_color)        
# no () in save_and_start() otherwise will execute it automatically before clicking the button
# binding multiple commands to the same button: command = lambda: [save_settings(), engine.start_engine()]


### DISPLAY WIDGETS
def display_widgets():
    # BASE VALUES
    # X
    x = 150
    x_button_gap = 170
    x_gap_for_path_objects = 5
    # Y
    y_base = 130
    y_gap = 30

    
    def y_location(gap_by_number):
        display_y = y_base + y_gap * gap_by_number
        return display_y

    # CLIPBOARD CHECKBOX
    checkbox['clipboard'][1].place(x=x, y=y_location(0))

    # POSTER CHECKBOX + ROLL DOWN BUTTON
    checkbox['poster'][1].place(x=x, y=y_location(1))
    poster_roll_down.place(x=x+x_button_gap, y=y_location(1))

    # LOOK FOR NATIVE TITLE + ROLL DOWN BUTTON
    checkbox['title'][1].place(x=x, y=y_location(2))
    title_search_roll_down.place(x=x+x_button_gap, y=y_location(2))

     # RAUN BY START CHECKBOX
    checkbox['run'][1].place(x=x, y=y_location(3))

    # CHROME DRIVER PATH - TITEL + FIELD + BUTTON
    chrome_driver_field_title.place(x=x+x_gap_for_path_objects, y=y_location(5))
    chrome_driver_field.place(x=x+x_gap_for_path_objects+3, y=y_location(5)+25)
    chrome_driver_button.place(x=x+x_gap_for_path_objects+x_button_gap, y=y_location(5)+13)

    # TARGET SHEET PATH - TITEL + FIELD + BUTTON
    target_sheet_field_title.place(x=x+x_gap_for_path_objects, y=y_location(7))
    target_sheet_field.place(x=x+x_gap_for_path_objects+3, y=y_location(7)+25)
    target_sheet_button.place(x=x+x_gap_for_path_objects+x_button_gap, y=y_location(7)+13)

    # NO PICTURE IN TARHET SHEET CHECKBOX
    checkbox['no_picture'][1].place(x=x+x_gap_for_path_objects, y=y_location(8)+13)

    # MOVIES DB SHEET PATH - TITEL + FIELD + BUTTON
    movies_db_sheet_field_title.place(x=x+x_gap_for_path_objects, y=y_location(10)-12)
    movies_db_sheet_field.place(x=x+x_gap_for_path_objects+3, y=y_location(10)+25-12)
    movies_db_sheet_button.place(x=x+x_gap_for_path_objects+x_button_gap, y=y_location(10)+13-12)

    # SAVE SETTINGS & START BUTTON
    button_save_and_start.place(x=x+x_gap_for_path_objects+30, y=y_location(12)+10)

    # SKINS ROLL DOWN BUTTON
    skins_roll_down.place(x=7, y=y_location(11))


display_widgets()

# START THE ENGINE AUTOMATICALLY WHEN THE run by start CHECKBOX VALUE SAVED AS 1/checked
if settings_data['run_by_start'] == 1:
    engine.start_engine()

window.mainloop()