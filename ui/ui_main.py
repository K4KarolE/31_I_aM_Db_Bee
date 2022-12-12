
from tkinter import *

root = Tk()

def click():
    #TEXT
    my_label1 = Label(root, text = 'Jumbo: ' + entry.get()) # entry.get() - printing text added in the entry
    my_label1.grid(column=20, row=25)

# BUTTON
my_button = Button(root, text ='My Button', padx=20, pady=20, command=click, fg='yellow', bg='red') # click (functions) without ()
my_button.grid(column=20, row=10)

# ENTRY - for 1. excel sheet route / 2. selenium route
entry = Entry(root, width=50, bg='grey', borderwidth=2)
entry.grid(column=20, row=9,)
entry.insert(0,'C3') # adding a default value to the entry / for excel - 1st cell


root.mainloop()