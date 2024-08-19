import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.geometry("464x400")
root.configure(bg="#DADADA")
root.resizable(False, False)

number = tk.StringVar()
number.initialize("")
number_font = ("Arial", 27)

entry = tk.Entry(root, textvariable=number, font=number_font, state="readonly")
entry.grid(row=0, column=0, columnspan=5, padx=10, ipady=15, sticky="WE")

counter=0

while counter<5:
    
    root.grid_columnconfigure(counter, weight=1)
    root.grid_rowconfigure(counter, weight=1)
    counter+=1

numbers_list=[]
operation=0
math_op=0
op_counter=False

#--------------------------defs-----------------------------------------------------------------------------

def change(num):
    
    if number.get()=="" or number.get()=="Syntax error" or number.get()=="MATH error":
        number.initialize(num)
    else:
        num_to_change=number.get()
        num_changed=num_to_change+num
        number.set(num_changed)
        
def operate(op):
    
    global operation
    global math_op
    global op_counter
    
    try:
        op_counter=True
        math_op=0
        operation=op
        first_num=number.get()
        numbers_list.append(float(first_num))
        number.initialize("")
    except ValueError:
        number.set("Syntax error")                         

def equal():    
                                         
    global operation
    global math_op
    global op_counter
    
    if op_counter:
        try:
            last_num=number.get()
            numbers_list.append(float(last_num))
            math_op=numbers_list[0]
            del numbers_list[0]
            
            if operation==1:
                for i in numbers_list:
                    math_op+=i
            elif operation==2:
                for i in numbers_list:
                    math_op-=i
            elif operation==3:
                for i in numbers_list:
                    math_op*=i
            elif operation==4:
                for i in numbers_list:
                    math_op/=i
            elif operation==5:                            
                for i in numbers_list:
                    math_op=math_op**i
            elif operation==6:                            
                for i in numbers_list:
                    math_op=i**(1/math_op)
                    
            if math_op==-0:
                math_op=0
    
            new_list=list(str(math_op))
            list_rev=new_list[::-1]
            new_list_2=[]
            
            for i in list_rev:
                if i!=".":
                    new_list_2.append(i)
                else:
                    break
                
            if new_list_2[0]=="0" and len(new_list_2)==1:
                number.set(str(int(math_op)))
            else:
                number.set(str(round(float(math_op), 22)))   
        except ZeroDivisionError:
            number.set("MATH error")
        except ValueError:
            number.set("")
    numbers_list.clear()
    operation=0
    
def delete():
    
    global operation
    global math_op
    
    number.initialize("")
    numbers_list.clear()
    math_op=0
    operation=0
    
#------------------------buttons-------------------------------------------------

button_0 = tk.Button(root, text="0", command=lambda: change("0"))
button_1 = tk.Button(root, text="1", command=lambda: change("1"))
button_2 = tk.Button(root, text="2", command=lambda: change("2"))
button_3 = tk.Button(root, text="3", command=lambda: change("3"))
button_4 = tk.Button(root, text="4", command=lambda: change("4"))
button_5 = tk.Button(root, text="5", command=lambda: change("5"))
button_6 = tk.Button(root, text="6", command=lambda: change("6"))
button_7 = tk.Button(root, text="7", command=lambda: change("7"))
button_8 = tk.Button(root, text="8", command=lambda: change("8"))
button_9 = tk.Button(root, text="9", command=lambda: change("9"))
button_subt_symbol = tk.Button(root, text="-", command=lambda: change("-"))
button_coma = tk.Button(root, text=".", command=lambda: change("."))

button_plus = tk.Button(root, text="+", command=lambda: operate(1))
button_subt = tk.Button(root, text="-", command=lambda: operate(2))
button_multi = tk.Button(root, text="*", command=lambda: operate(3))
button_div = tk.Button(root, text="/", command=lambda: operate(4))
button_exp = tk.Button(root, text="^", command=lambda: operate(5))
button_base = tk.Button(root, text="√", command=lambda: operate(6))
button_equal = tk.Button(root, text="=", command=equal)
button_delete = tk.Button(root, text="DEL", command=delete)

#------------------------------------button-grid-------------------------------------------------

button_7.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW")
button_8.grid(row=1, column=1, padx=5, pady=5, sticky="NSEW")
button_9.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
button_exp.grid(row=1, column=3, padx=5, pady=5, sticky="NSEW")
button_base.grid(row=1, column=4, padx=5, pady=5, sticky="NSEW")

button_4.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
button_5.grid(row=2, column=1, padx=5, pady=5, sticky="NSEW")
button_6.grid(row=2, column=2, padx=5, pady=5, sticky="NSEW")
button_multi.grid(row=2, column=3, padx=5, pady=5, sticky="NSEW")
button_div.grid(row=2, column=4, padx=5, pady=5, sticky="NSEW")

button_1.grid(row=3, column=0, padx=5, pady=5, sticky="NSEW")
button_2.grid(row=3, column=1, padx=5, pady=5, sticky="NSEW")
button_3.grid(row=3, column=2, padx=5, pady=5, sticky="NSEW")
button_plus.grid(row=3, column=3, padx=5, pady=5, sticky="NSEW")
button_subt.grid(row=3, column=4, padx=5, pady=5, sticky="NSEW")

button_coma.grid(row=4, column=0, padx=5, pady=5, sticky="NSEW")
button_0.grid(row=4, column=1, padx=5, pady=5, sticky="NSEW")
button_subt_symbol.grid(row=4, column=2, padx=5, pady=5, sticky="NSEW")
button_equal.grid(row=4, column=3, padx=5, pady=5, sticky="NSEW")
button_delete.grid(row=4, column=4, padx=5, pady=5, sticky="NSEW")

root.mainloop()
