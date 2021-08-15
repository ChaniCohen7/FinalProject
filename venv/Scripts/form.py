from tkinter import *
from tkinter import ttk
from logic import *

class form():

    def __init__(self):

        self.l=logic()
        self.current_date=self.l.data_json["date"].split('-')

        self.ws = Tk()
        self.ws.title("Convert Money")
        self.ws.geometry('800x500')
        self._convert_from=self.convert_from()
        self._convert_to=self.convert_to()
        self._money=self.money()
        self._update_to_show=self.update_to_show()
        self._btn=self.btn()
        self._result=self.result()
        self.ws.mainloop()




    def convert_from(self):
        self.convert_from = Label(self.ws, text="convert_from: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        self.coins_value = list(self.l.data_json["rates"].keys())
        self.convert_from1 = ttk.Combobox(self.ws,values=self.coins_value, width=26)
        self.convert_from1.current(0)
        self.convert_from.place(relx=0.2, rely=0.3, anchor='center')
        self.convert_from1.place(relx=0.2, rely=0.4, anchor='center')

    def convert_to(self):
        convert_to = Label(self.ws, text="convert_to: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        coins_value = list(self.l.data_json["rates"].keys())
        self.convert_to1 = ttk.Combobox(self.ws,values=coins_value, width=26)
        self.convert_to1.current(0)
        convert_to.place(relx=0.8, rely=0.3, anchor='center')
        self.convert_to1.place(relx=0.8, rely=0.4, anchor='center')

    def update_to_show(self):

        self.update_to_show="last update on: "+self.current_date[2]+'/'+self.current_date[1]+'/'+self.current_date[0]
        self.last_update = Label(self.ws, text=self.update_to_show, anchor="w",bg="red", fg="white",bd="10",width=26)

    def money(self):
        money = Label(self.ws, text="money: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        self.money1 = Entry(self.ws,width=26)
        money.place(relx=0.5, rely=0.5, anchor='center')
        self.money1.place(relx=0.5, rely=0.6, anchor='center')

    def btn(self):
        btn = Button(self.ws, text="Convert",command=self.l.click(self.convert_from1,self.convert_to1,self.money1),bg="red", fg="white",bd="10",width=26)
        btn.place(relx=0.5, rely=0.7, anchor='center')
    def result(self):
        self.ws.result = Label(self.ws, text="result:", anchor="w", bg="red", fg="white",bd="10",width=26)
        self.ws.result.place(relx = 0.5,rely = 0.8,anchor = 'center')
    def last_update(self):
        last_update.place(relx = 0.5,rely = 0.15,anchor = 'center')

