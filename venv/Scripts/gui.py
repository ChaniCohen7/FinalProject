from convertions import  *
from urllib.request import urlopen
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import *
import os
class gui():
    ws = Tk()
    ws.title('Python Guides')
    ws.geometry('9000x9000')
    ws.config(bg='#1bafb8')

    f = Frame(ws,padx=200, pady=80)
    current_date=data_json["date"].split('-')
    update_to_show="last update on: "+current_date[2]+'/'+current_date[1]+'/'+current_date[0]
    last_update = Label(ws, text=update_to_show, anchor="w",bg="red", fg="blue",bd="10")
    last_update.pack(fill="x",padx=20, pady=20)

    convert_from = Label(ws, text="convert_from: ", anchor="w",bg="red", fg="blue",bd="10")
    convert_from.pack(fill="x",padx=100, pady=10)
    coins_value = list(data_json["rates"].keys())
    convert_from1 = ttk.Combobox(ws,values=coins_value)
    convert_from1.pack()
    convert_from1.current(0)

    convert_to = Label(ws, text="convert_to: ", anchor="w",bg="red", fg="blue",bd="10")
    convert_to.pack(fill="x" ,padx=100, pady=20)
    coins_value = list(data_json["rates"].keys())
    convert_to1 = ttk.Combobox(ws,values=coins_value)
    convert_to1.pack()
    convert_to1.current(0)


    money = Label(ws, text="money: ", anchor="w",bg="red", fg="blue",bd="10")
    money.pack(fill="x",padx=100, pady=30)
    money1 = Entry(ws,width="30")
    money1.pack(padx=100, pady=35)
    btn = Button(ws, text="Convert",command=click,bg="red", fg="blue",bd="10")
    btn.pack(fill="x")
    f.pack(padx=200, pady=40)
    ws.result = Label(ws, text="result:", anchor="w", bg="red", fg="blue",bd="10")
    ws.result.pack(fill="x", padx=100, pady=10)

    last_update.place(relx = 0.5,rely = 0.7,anchor = 'center')


    convert_from.place(relx = 0.2,rely = 0.2,anchor = 'center')
    convert_from1.place(relx = 0.2,rely = 0.3,anchor = 'center')

    convert_to.place(relx = 0.8,rely = 0.2,anchor = 'center')
    convert_to1.place(relx = 0.8,rely = 0.3,anchor = 'center')

    money1.place(relx = 0.5,rely = 0.5,anchor = 'sw')
    money.place(relx = 0.5,rely = 0.3,anchor = 'center')
    money1.place(relx = 0.5,rely = 0.4,anchor = 'center')
    btn.place(relx = 0.5,rely = 0.5,anchor = 'center')
    ws.result.place(relx = 0.5,rely = 0.6,anchor = 'center')
    ws.mainloop()


