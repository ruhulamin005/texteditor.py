from tkinter import *
from tkinter import filedialog
import sqlite3
import re
import random
import string
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst


root = Tk()
root.title('Read & Write window')
root.geometry("500x450")

###cust_name = StringVar()
#cust_num = StringVar()
#bill_no = IntVar()
#bill_details = StringVar()
#bill_date = StringVar()###


#Connecting with database

with sqlite3.connect("store.db") as db:
    cur = db.cursor()






def open_txt():
	text_file = filedialog.askopenfilename(initialdir="D:",title="Open Text File", filetypes=(("Text Files","*.txt"), ))
	text_file = open("sample.txt", 'w')
	#stuff = 
	text_file.write("Hello there hi 5")

	#my_text.insert(END, stuff)

	#Working With database:
	#query
	bill_info = ("SELECT * from bill ORDER BY bill_no DESC LIMIT 1")
	cur.execute(bill_info)
	result = cur.fetchone()
	print(result)

	bill_no = result[0]
	bill_date = result[1]
	cust_name = result[2]
	cust_num = result[3]
	bill_details = result[4]

	print(bill_no)
	print(bill_date)
	print(cust_name)
	print(cust_num)
	print(bill_details)



my_text = Text(root,width=40, height=10, font="Helvetica,16")
my_text.pack(pady=20)

open_button = Button(root, text="Open Text File", command = open_txt)
open_button.pack(pady=20)



root.mainloop()