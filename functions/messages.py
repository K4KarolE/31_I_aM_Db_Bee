#!/bin python3.11

import tkinter.messagebox  


error_popup_window_title = [
    'Got stuck in honey',
    'Danger Will Robinson, danger!'
    ]

popup_message_dic = {
    'wrong_link': 'Wrong link in clipboard\n\nCopy the IMDb link and click OK',
    'excel_is_open':'Close your sheet and click OK',
    'bye_bye':'You just blew it honey!'
    }

def error_pop_up(popup_message_dic_key):
    tkinter.messagebox.showinfo(error_popup_window_title[0], f"{popup_message_dic[popup_message_dic_key]}")

# error_pop_up('wrong_link')
# error_pop_up('excel_is_open')


### TERMINAL MESSAGES
import shutil
terminal_columns = shutil.get_terminal_size().columns

frame = { 'bee_noise': ' Z-z-z ',
            'error': ' * '}

message_dic = { 'banner': ' I aM D bee! ',
            'outro': ' Honey added to your jar! ',
            'error_link': 'ERROR - WRONG IMDb LINK - COPY AGAIN & HIT ENTER ',
            'error_decider': 'ERROR - DECIDER ',
            'error_movie_title':' ERROR - MOVIE TITLE ',
            'error_year':'ERROR - YEAR OF RELEASE',
            'error_stars':'ERROR - STARS',
            'error_length':'ERROR - LENGTH',
            'error_excel':'ERROR - Close your sheet and hit Enter',
            'error_poster':'ERROR - ERROR - POSTER',}


def message(frame_type, frame_length_adjuster, message_type):
    message_length = len(message_dic[message_type])
    frame_type_length = len(frame[frame_type])
    print('\n')
    print((frame[frame_type] * int(message_length / frame_type_length * frame_length_adjuster)).center(terminal_columns))  # message('bee_noise', 2, 'banner')
    print()
    print(message_dic[message_type].center(terminal_columns))
    print()
    print((frame[frame_type] * int(message_length / frame_type_length * frame_length_adjuster)).center(terminal_columns))
    print('\n')