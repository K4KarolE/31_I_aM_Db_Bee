
import shutil

terminal_columns = shutil.get_terminal_size().columns

frame = { 'bee_noise': ' Z-z-z ',
            'error': ' * '}

message_dic = { 'banner': ' I aM D bee! ',
            'outro': ' Honey added to your jar! ',
            'error_link': 'ERROR - WRONG IMDb LINK ',
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


def tv_show_length():
    note_length = len('TV Mini Series: length of the whole show')
    print()
    print(' Please note '.center(terminal_columns))
    print(('*'*note_length).center(terminal_columns))
    print('TV Series: length of an episode'.ljust(note_length).center(terminal_columns))
    print('TV Mini Series: length of the whole show'.center(terminal_columns))
    print('Will be added to the sheet.'.center(terminal_columns))
    print(('*'*note_length).center(terminal_columns))
    print()


message('bee_noise', 2, 'banner')
message('bee_noise', 1.5, 'outro')
message('error', 1.2, 'error_excel')
message('error', 2, 'error_stars')