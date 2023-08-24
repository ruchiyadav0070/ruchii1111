import tkinter as tk
def calculate():
    try:
        result=eval(expression.get())
        expression.set(str(result))
    except Exception as e:
        expression.set("Error")
def button_click(value):
    current_expression=expression.get()
    new_expression=current_expression + str(value)
    expression.set(new_expression)
def all_clear_expression():
    expression.set("")
def delete_last_character():
    current_expression=expression.get()
    new_expression=current_expression[:-1]
    expression.set(new_expression)
def add_decimal_point():
    current_expression=expression.get()
    if current_expression and current_expression[-1].isdigit():
        new_expression=current_expression +"."
        expression.set(new_expression)
window=tk.Tk()
window.title("Calculator")
window.configure(bg="white")
expression=tk.StringVar()
expression.set("")
entry=tk.Entry(window,textvariable=expression,justify="right")
entry.grid(row=0,column=10,padx=10,pady=10)
entry.configure(fg="black",bg="white",font=("Arial",14,"bold" ))
for i in range(1,10):
    button=tk.Button(window,text=str(i),width=10,command=lambda num=i: button_click(num))
    button.grid(row=(i-1)//3+1,column=(i-1)%3,padx=2,pady=2)
    button.configure(fg="black",bg="darkgray",font=("Arial",12,"bold"))
zero_button=tk.Button(window,text="0",width=10,command=lambda num=i: button_click(0))
zero_button.grid(row=4,column=1,padx=5,pady=5)
zero_button.configure(fg="black",bg="darkgray",font=("Arial",12,"bold"))
operators=['*','-','+','/']
for i in range(len(operators)):
    button=tk.Button(window,text=operators[i],width=10,command=lambda op=operators[i]: button_click(op))
    button.grid(row=(i+1),column=3,padx=5,pady=5)
    button.configure(fg="black",bg="darkgray",font=("Arial",12,"bold"))
equals_button=tk.Button(window,text="=",width=10,command=calculate)
equals_button.grid(row=4,column=2,padx=5,pady=5)
equals_button.configure(fg="black",bg="darkgray",font=("Arial",12,"bold"))

decimal_button=tk.Button(window,text=".",width=10,command=add_decimal_point)
decimal_button.grid(row=4,column=0,padx=5,pady=5)
decimal_button.configure(fg="black",bg="darkgray",font=("Arial",12,"bold"))

all_clear_button=tk.Button(window,text="C",width=10,command=all_clear_expression)
all_clear_button.grid(row=0,column=0,padx=5,pady=5)
all_clear_button.configure(fg="black",bg="white",font=("Arial",12,"bold"))

delete_button=tk.Button(window,text="del",width=10,command=delete_last_character)
delete_button.grid(row=0,column=3,padx=5,pady=5)
delete_button.configure(fg="black",bg="white",font=("Arial",12,"bold"))

window.mainloop()










    

    

  

               


                  
















































                   



               
        
                        
        
                        
    
