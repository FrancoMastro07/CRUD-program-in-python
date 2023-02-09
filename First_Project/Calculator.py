from tkinter import *

#----------------root-------------------

root=Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")


#-------------frame--------------------------------------

frame=Frame(root)
frame.pack()

#-------------entry---------------------------------------

ScreenNumber=StringVar()
entry_number=Entry(frame, width=30, textvariable=ScreenNumber)
entry_number.grid(row=1, column=1, padx=10, pady=10, columnspan=6)
entry_number.config(background="black", fg="#03f943", justify="right")

#------------------------code-----------------------------------------

reset_screen=False

operation=""

result=0

def Clicked_Num(num):

	global reset_screen

	if reset_screen!=False:

		ScreenNumber.set(num)

		reset_screen=False

	else:

		return ScreenNumber.set(ScreenNumber.get()+num)

def sum(num):

	global operation

	global result

	global reset_screen

	result+=int(num)

	operation="suma"

	reset_screen=True

	ScreenNumber.set(result)

num1=0

clicker_rest=0

def rest(num):

	global operation

	global result

	global reset_screen

	global num1

	global clicker_rest

	if clicker_rest==0:

		num1=int(num)

		result=num1

	else:

		if clicker_rest==1:

			result=num1-int(num)

		else:

			result=int(result)-int(num)

		ScreenNumber.set(result)
		
		result=ScreenNumber.get()

	clicker_rest+=1

	operation="rest"

	reset_screen=True	

def results():

	global result

	global operation

	if "suma" in operation:

		ScreenNumber.set(result+int(ScreenNumber.get()))

		result=0

	elif "rest" in operation:

		ScreenNumber.set(int(result)-int(ScreenNumber.get()))

		result=0

		clicker_rest=0


	
#----------------buttons--------------------------------------------------------

button_7=Button(frame, text="7", width=3, command=lambda:Clicked_Num("7"))
button_7.grid(row=2, column=1, padx=10, pady=10)

button_8=Button(frame, text="8", width=3, command=lambda:Clicked_Num("8"))
button_8.grid(row=2, column=2, padx=10, pady=10)

button_9=Button(frame, text="9", width=3, command=lambda:Clicked_Num("9"))
button_9.grid(row=2, column=3, padx=10, pady=10)

button_4=Button(frame, text="4", width=3, command=lambda:Clicked_Num("4"))
button_4.grid(row=3, column=1, padx=10, pady=10)

button_5=Button(frame, text="5", width=3, command=lambda:Clicked_Num("5"))
button_5.grid(row=3, column=2, padx=10, pady=10)

button_6=Button(frame, text="6", width=3, command=lambda:Clicked_Num("6"))
button_6.grid(row=3, column=3, padx=10, pady=10)

button_1=Button(frame, text="1", width=3, command=lambda:Clicked_Num("1"))
button_1.grid(row=4, column=1, padx=10, pady=10)

button_2=Button(frame, text="2", width=3, command=lambda:Clicked_Num("2"))
button_2.grid(row=4, column=2, padx=10, pady=10)

button_3=Button(frame, text="3", width=3, command=lambda:Clicked_Num("3"))
button_3.grid(row=4, column=3, padx=10, pady=10)

button_0=Button(frame, text="0", width=3, command=lambda:Clicked_Num("0"))
button_0.grid(row=5, column=2, padx=10, pady=10)

button_sum=Button(frame, text="+", width=3, command=lambda:sum(ScreenNumber.get()))
button_sum.grid(row=2, column=4, padx=10, pady=10)

button_x=Button(frame, text="x", width=3, command=lambda:Clicked_Num("x"))
button_x.grid(row=3, column=4, padx=10, pady=10)

button_delete=Button(frame, text="Del", width=3, command=lambda:ScreenNumber.set(""))
button_delete.grid(row=4, column=4, padx=10, pady=10)

button_rest=Button(frame, text="-", width=3, command=lambda:rest(ScreenNumber.get()))
button_rest.grid(row=2, column=5, padx=10, pady=10)

button_div=Button(frame, text="/", width=3, command=lambda:Clicked_Num("/"))
button_div.grid(row=3, column=5, padx=10, pady=10)

button_equal=Button(frame, text="=", width=3, command=lambda:results())
button_equal.grid(row=4, column=5, padx=10, pady=10)

#--------------------------end---------------------------------------------

root.mainloop()