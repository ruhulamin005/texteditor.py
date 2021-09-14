#from tkinter import *
from tkinter import *
from tkinter import filedialog
from tkinter import font


root = Tk()

root.title('Ruhul Er Text Editor')
root.geometry("1200x600")


#main frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# creating a scroll bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill=Y)

# text box

my_text = Text(my_frame,width=97, height = 25, font=("Helvetica",16),selectbackground = "yellow",selectforeground = "black",undo = True,yscrollcommand = text_scroll.set)
my_text.pack()

# Configure scrollbar

text_scroll.config(command=my_text.yview)


#Creating a menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add a file menu for GUI 
file_menu = Menu(my_menu)
my_menu.add_cascade(label = "File", menu=file_menu)

file_menu.add_command(label = "New")
file_menu.add_command(label = "Open")
file_menu.add_command(label = "Save")

file_menu.add_separator()
file_menu.add_command(label = "Exit")

#Edit Menu


#edit_menu = Menu(my_menu)
#root.config(menu=edit_menu)

#Add a file menu for GUI 
edit_menu = Menu(my_menu)
my_menu.add_cascade(label = "Edit", menu=edit_menu)

edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo")



root.mainloop()

