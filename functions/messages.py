
import shutil

terminal_columns = shutil.get_terminal_size().columns

bee_noise = ' Z-z-z '

def frame(k):
    print()
    print((bee_noise*k).center(terminal_columns))
    print()

def banner():
    k = 11
    frame(k)
    print(' I aM D bee! '.center(terminal_columns))
    frame(k)

def outro():
    k = 6
    frame(k)
    print(' Honey added to your jar! '.center(terminal_columns))
    frame(k)

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

def link_error():
    k = 6
    frame(k)
    print(' Wrong IMDb link! '.center(terminal_columns))
    frame(k)