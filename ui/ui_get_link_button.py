import pyperclip
from tkinter import *

root = Tk()

def get_link():
    link = pyperclip.paste()
    my_label1 = Label(root, text = 'Your link: ' + link) 
    my_label1.grid(column=20, row=25)

my_button = Button(root, text =' Get the link ', padx=20, pady=20, command=get_link)
my_button.grid(column=20, row=10)


root.mainloop()