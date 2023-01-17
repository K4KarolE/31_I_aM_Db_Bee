
from tkinter import *
 
from tkinter import filedialog
 
def browseFiles():
  filename = filedialog.askopenfilename(initialdir = "/",
            title = "Select a File",
            filetypes = (("Excel sheet", "*.xlsx"),
                           ("all files", "*.*")))
   
  # Change label contents
  label_file_explorer.configure(text=filename)

                                                  
window = Tk()

window.title('File Explorer')

window.geometry("500x500")

window.config(background = "white")



button_explore = Button(window,
text = "Browse Files",
command = browseFiles)

label_file_explorer = Label(window, text ="filename",
height = 2)

label_file_explorer.pack()
button_explore.pack()




window.mainloop()