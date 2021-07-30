from tkinter import *

def click():
    val = convert_from["text"]
    print(val)
f = Frame()
convert_from = Label(f, text="convert_from: ", anchor="w")
convert_from.pack(fill="x")
convert_from = Entry(f)
convert_from.pack()
convert_to = Label(f, text="convert_to: ", anchor="w")
convert_to.pack(fill="x")
convert_to = Entry(f)
convert_to.pack()
money = Label(f, text="money: ", anchor="w")
money.pack(fill="x")
money = Entry(f)

