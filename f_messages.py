
import shutil

terminal_columns = shutil.get_terminal_size().columns

def banner():
    print()
    k = 11
    print((' Z-z-z '*k).center(terminal_columns))
    print()
    print(' I aM D bee! '.center(terminal_columns))
    print()
    print((' Z-z-z '*k).center(terminal_columns))
    print('\n')

def outro():
    k = 6
    print()
    print((' Z-z-z '*k).center(terminal_columns))
    print()
    print(' Honey added to your jar! '.center(terminal_columns))
    print()
    print((' Z-z-z '*k).center(terminal_columns))
    print()

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