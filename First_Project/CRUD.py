from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess

#----------------------database-code----------------------------------------------#


def connection():	

	connection=sqlite3.connect("CRUD")
	slider=connection.cursor()
	
	try:

		slider.execute(""" 

		CREATE TABLE USERSDATA (

			ID INTEGER PRIMARY KEY AUTOINCREMENT, 
			NAME VARCHAR(50),
			PASSWORD VARCHAR(50),
			SURNAME VARCHAR(10),
			ADDRESS VARCHAR(50),
			COMMENTS VARCHAR(100))

			""")

		messagebox.showinfo("Connect a database", "The database was succesfully created")


	except:
	
		messagebox.showwarning("Connect a database", "A database has already been created")	
	
def quit():

	quit_value=messagebox.askokcancel("Quit", "Do you want to quit?")

	if quit_value==True:

		root.destroy()

def delete_fields():

	if True:

		Id.set("")
		Name.set("")
		Password.set("") 
		Surname.set("")
		Address.set("")
		comments_text.delete("1.0", END)

def create():

	try:
		connection=sqlite3.connect("CRUD")
		slider=connection.cursor()
		slider.execute("INSERT INTO USERSDATA VALUES (NULL, '" + Name.get() + "','" + Password.get() + "','" + Surname.get() + "','" + Address.get() + "','" + comments_text.get("1.0", END) + "')")
		connection.commit()
		messagebox.showinfo("Create a table", "A table was succesfully created")

	except sqlite3.OperationalError as e:

		if "no such table: USERSDATA" in str(e):

			messagebox.showwarning("Error", "There is no database created")

		else:

			messagebox.showwarning("Error", "Unknown error")

def read():

	
	try:
		connection=sqlite3.connect("CRUD")
		slider=connection.cursor()
		slider.execute("SELECT * FROM USERSDATA WHERE ID=" + Id.get())
		information=slider.fetchall()

		for info in information:

			Id.set(info[0])
			Name.set(info[1])
			Password.set(info[2])
			Surname.set(info[3])
			Address.set(info[4])
			comments_text.insert("1.0", info[5])

		connection.commit()
		messagebox.showinfo("Read a table", "The table was succesfully read")

	except sqlite3.OperationalError as e:

		if "incomplete input" in str(e):

			messagebox.showwarning("Error", "There is no database created")

		else:

			messagebox.showwarning("Error", "Unknown error")	

def update():

	try:
		connection=sqlite3.connect("CRUD")
		slider=connection.cursor()
		data=Name.get(), Password.get(), Surname.get(), Address.get(), comments_text.get("1.0", END)

		slider.execute("UPDATE USERSDATA SET NAME=?, PASSWORD=?, SURNAME=?, ADDRESS=?, COMMENTS=? " + "WHERE ID=" + Id.get(), (data))
		
		connection.commit()
		messagebox.showinfo("Update", "The update was succesfully done")

	except sqlite3.OperationalError as e:

		if "incomplete input" in str(e):

			messagebox.showwarning("Error", "There is no database created")

		else:

			messagebox.showwarning("Error", "Unknown error")	

def delete():

	try:
		connection=sqlite3.connect("CRUD")
		slider=connection.cursor()

		slider.execute("DELETE FROM USERSDATA WHERE ID=" + Id.get())
		connection.commit()
		delete_info=messagebox.askokcancel("Delete information", "Do you want to delete it?")

		if delete_info==True:

			messagebox.showinfo("Delete information", "The information was succesfully deleted")

	except sqlite3.OperationalError as e:
		
		if "incomplete input" in str(e):

			messagebox.showwarning("Error", "There is no database created")

		else:

			messagebox.showwarning("Error", "Unknown error")				

def license():

	messagebox.showinfo("License", "Open license")

def open_calculator():

	subprocess.Popen(["python", "Calculator.py"])

#--------------root----------------------------------------------#

root=Tk()

#--------interface-----------------------------------------------#

root.title("CRUD")
root.iconbitmap("database.ico")
root.geometry("300x600")

bar_menu=Menu(root)
root.config(menu=bar_menu, width=300, height=300)

#--------------menu----------------------------------------------#

menu_BBDD=Menu(bar_menu, tearoff=0)
menu_BBDD.add_command(label="Connect", command=connection)
menu_BBDD.add_command(label="Quit", command=quit)
bar_menu.add_cascade(label="BBDD", menu=menu_BBDD)

menu_delete=Menu(bar_menu, tearoff=0)
menu_delete.add_command(label="Delete fields", command=delete_fields)
bar_menu.add_cascade(label="Delete", menu=menu_delete)

menu_CRUD=Menu(bar_menu, tearoff=0)
menu_CRUD.add_command(label="Create", command=create)
menu_CRUD.add_command(label="Read", command=read)
menu_CRUD.add_command(label="Update", command=update)
menu_CRUD.add_command(label="Delete", command=delete)
bar_menu.add_cascade(label="CRUD", menu=menu_CRUD)

menu_tools=Menu(bar_menu, tearoff=0)
menu_tools.add_command(label="calculator", command=open_calculator)
bar_menu.add_cascade(label="Tools", menu=menu_tools)

menu_help=Menu(bar_menu, tearoff=0)
menu_help.add_command(label="License", command=license)
bar_menu.add_cascade(label="Help", menu=menu_help)

#-------frame------------------------------------------------------#

myframe=Frame(root)
myframe.pack()
myframe.config()

#--------entry-and-scrollbar------------------------------------------#

Id=StringVar()
id_text=Entry(myframe, textvariable=Id)
id_text.grid(row=0, column=1)
id_text.config(bg="#A9EBBB", justify="center")

Name=StringVar()
name_text=Entry(myframe, textvariable=Name)
name_text.grid(row=1, column=1)
name_text.config(bg="#A9EBBB", justify="center")

Password=StringVar()
password_text=Entry(myframe, textvariable=Password)
password_text.grid(row=2, column=1)
password_text.config(bg="#A9EBBB", justify="center", show="*")

Surname=StringVar()
surname_text=Entry(myframe, textvariable=Surname)
surname_text.grid(row=3, column=1)
surname_text.config(bg="#A9EBBB", justify="center")

Address=StringVar()
address_text=Entry(myframe, textvariable=Address)
address_text.grid(row=4, column=1)
address_text.config(bg="#A9EBBB", justify="center")

comments_text=Text(myframe, width=16, height=5)
comments_text.grid(row=5, column=1)
comments_text.config(bg="#A9EBBB")

scrollvert=Scrollbar(myframe, command=comments_text.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")
comments_text.config(yscrollcommand=scrollvert.set)

#----------label--------------------------------------------------------#

id_label=Label(myframe, text="Id: ")
id_label.grid(row=0, column=0, sticky="s", padx=30, pady=30)

name_label=Label(myframe, text="Name: ")
name_label.grid(row=1, column=0, sticky="s", padx=30 , pady=30)

password_label=Label(myframe, text="Password: ")
password_label.grid(row=2, column=0, sticky="s", padx=30 , pady=30)

surname_label=Label(myframe, text="Surname: ")
surname_label.grid(row=3, column=0, sticky="s", padx= 30 , pady=30)

address_label=Label(myframe, text="Address: ")
address_label.grid(row=4, column=0, sticky="s", padx=30 , pady=30)

comments_label=Label(myframe, text="Comments: ")
comments_label.grid(row=5, column=0, sticky="s", padx=30 , pady=30)

#------------button------------------------------------------------------#

button_create=Button(root, text="Create", command=create)
button_create.pack(side="left", padx=15, pady=15)

button_read=Button(root, text="Read", command=read)
button_read.pack(side="left", padx=15, pady=15)

button_delete=Button(root, text="Delete", command=delete)
button_delete.pack(side="right", padx=15, pady=15)

button_update=Button(root, text="Update", command=update)
button_update.pack(side="right", padx=15, pady=15)

#----------------end---------------------------------------------------------------#

root.mainloop()



