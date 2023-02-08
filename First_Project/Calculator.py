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

#----------------buttons--------------------------------------------------------

button_7=Button(frame, text="7", width=3, command=lambda:ScreenNumber.set("7"))
button_7.grid(row=2, column=1, padx=10, pady=10)

button_8=Button(frame, text="8", width=3, command=lambda:ScreenNumber.set("8"))
button_8.grid(row=2, column=2, padx=10, pady=10)

button_9=Button(frame, text="9", width=3, command=lambda:ScreenNumber.set("9"))
button_9.grid(row=2, column=3, padx=10, pady=10)

button_4=Button(frame, text="4", width=3, command=lambda:ScreenNumber.set("4"))
button_4.grid(row=3, column=1, padx=10, pady=10)

button_5=Button(frame, text="5", width=3, command=lambda:ScreenNumber.set("5"))
button_5.grid(row=3, column=2, padx=10, pady=10)

button_6=Button(frame, text="6", width=3, command=lambda:ScreenNumber.set("6"))
button_6.grid(row=3, column=3, padx=10, pady=10)

button_1=Button(frame, text="1", width=3, command=lambda:ScreenNumber.set("1"))
button_1.grid(row=4, column=1, padx=10, pady=10)

button_2=Button(frame, text="2", width=3, command=lambda:ScreenNumber.set("2"))
button_2.grid(row=4, column=2, padx=10, pady=10)

button_3=Button(frame, text="3", width=3, command=lambda:ScreenNumber.set("3"))
button_3.grid(row=4, column=3, padx=10, pady=10)

button_0=Button(frame, text="0", width=3, command=lambda:ScreenNumber.set("0"))
button_0.grid(row=5, column=2, padx=10, pady=10)

button_sum=Button(frame, text="+", width=3, command=lambda:ScreenNumber.set("+"))
button_sum.grid(row=2, column=4, padx=10, pady=10)

button_x=Button(frame, text="x", width=3, command=lambda:ScreenNumber.set("x"))
button_x.grid(row=3, column=4, padx=10, pady=10)

button_delete=Button(frame, text="Del", width=3, command=lambda:ScreenNumber.set(""))
button_delete.grid(row=4, column=4, padx=10, pady=10)

button_rest=Button(frame, text="-", width=3, command=lambda:ScreenNumber.set("-"))
button_rest.grid(row=2, column=5, padx=10, pady=10)

button_div=Button(frame, text="/", width=3, command=lambda:ScreenNumber.set("/"))
button_div.grid(row=3, column=5, padx=10, pady=10)

button_equal=Button(frame, text="=", width=3, command=lambda:ScreenNumber.set("="))
button_equal.grid(row=4, column=5, padx=10, pady=10)

#--------------------------end---------------------------------------------

root.mainloop()