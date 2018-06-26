

import Tkinter as tk
from functools import partial


def call_result(label_a, label_b, label_c, label_d, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    a = float(num1) + float(num2)
    b = float(num1) - float(num2)
    c = float(num1) * float(num2)
    d = float(num1) / float(num2)
    label_a.config(bg="light blue",text="Addition is %f" % a)
    label_b.config(bg="light blue",text="Subtraction is %f" % b)
    label_c.config(bg="light blue",text="Multiplication is %f" % c)
    label_d.config(bg="light blue",text="Division is %f" % d)
    return


root = tk.Tk()
root.geometry('400x300+100+200')
root.title('Simple Calculator')
root.configure(background="light blue")
number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root,bg="light blue", padx=16, bd=8, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root,bg="light blue", padx=16, bd=8, text="Enter a number").grid(row=1, column=0)
labelNum2 = tk.Label(root,bg="light blue", padx=16, bd=8,text="Enter another number").grid(row=2, column=0)
label_a = tk.Label(root)
label_b = tk.Label(root)
label_c = tk.Label(root)
label_d = tk.Label(root)
label_a.grid(row=7, column=2)
label_b.grid(row=8, column=2)
label_c.grid(row=9, column=2)
label_d.grid(row=10, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, label_a, label_b, label_c, label_d, number1, number2)
buttonCal = tk.Button(root, text="Calculator", bg="powder blue", padx=16, bd=8, command=call_result).grid(row=3, column=2)
root.mainloop()