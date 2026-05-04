import tkinter as tk
from tkinter import StringVar

main_window= tk.Tk()
main_window.geometry("312x324")
main_window.title('My_Calculator')

expression = ""
input_text=StringVar()

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""
#top frame
input_frame= tk.Frame(main_window, width=312, height=50, bd=0, highlightbackground="black",
                      highlightcolor="black", highlightthickness=1)
#pact the frame using pack()
input_frame.pack(side='top')

input_field=tk.Entry(input_frame, font=('arial',18, 'bold'), textvariable=input_text, width=50,
                     bg='#eee', bd=0, justify='right')

input_field.grid(row=0,column=0)
input_field.grid(ipady=10)

#buttons
btns_frame = tk. Frame(main_window, width=312, height=272.5, bg="grey")
btns_frame. pack()

# The next row includes 2 buttons, 'Clear (Clear)' and 'Divide (/)':

#Create a button widget called btn_clearing
btn_clearing=tk. Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="#eee",
cursor="hand2", command=btn_clear)

#position the button clear in the grid
btn_clearing.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

#Create a button for the division operator called btn_div
btn_div=tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=lambda: btn_click("/"))

#position the button div in the grid
btn_div.grid(row=0,column=3, padx=1, pady=1)

#includes 4 buttons, '7', '8', '9' and 'Multiply (*)':
tk. Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
tk. Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
tk. Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
tk. Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

#includes 4 buttons, '4', '5', '6' and 'Subtract (-)':
tk. Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
tk. Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
tk. Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
tk. Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

#bottom frame includes 4 buttons, '1', '2', '3', and 'plus (+)':
tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

#includes 3 buttons, '0', 'Decimal (.)', and 'Equal To (=)':
tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, pady=1)
tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
cursor="hand2", command=btn_equal).grid(row=4, column=3, padx=1, pady=1)

main_window.mainloop()


