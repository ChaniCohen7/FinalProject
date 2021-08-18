from tkinter import *
from tkinter import ttk
from logic import *
from datetime import *

class form():

    def __init__(self):

        self.l=logic()
        self.current_date=self.l.data_json["date"].split('-')
        self.ws = Tk()
        self.ws.title("Convert Money")
        self.ws.geometry('800x500')
        self.convert_from=self.init_convert_from()
        self.convert_from1=self.init_convert_from1()
        self.convert_to=self.init_convert_to()
        self.convert_to1=self.init_convert_to1()
        self.money=self.init_money()
        self.money1=self.init_money1()
        self.last_update=self.init_last_update()
        self.btn=self.init_btn()
        self.result=self.init_result()
        self.ws.mainloop()




    def init_convert_from(self):
        self.convert_from = Label(self.ws, text="convert_from: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        self.coins_value = list(self.l.data_json["rates"].keys())
        self.convert_from.place(relx=0.2, rely=0.3, anchor='center')
        return self.convert_from

    def init_convert_from1(self):
        self.convert_from1 = ttk.Combobox(self.ws, values=self.coins_value, width=26)
        self.convert_from1.current(0)
        self.convert_from1.place(relx=0.2, rely=0.4, anchor='center')
        return self.convert_from1
    def init_convert_to(self):
        convert_to = Label(self.ws, text="convert_to: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        coins_value = list(self.l.data_json["rates"].keys())
        convert_to.place(relx=0.8, rely=0.3, anchor='center')

    def init_convert_to1(self):
        self.convert_to1 = ttk.Combobox(self.ws, values=self.coins_value, width=26)
        self.convert_to1.current(0)
        self.convert_to1.place(relx=0.8, rely=0.4, anchor='center')
        return self.convert_to1
    def init_update_to_show(self):
        self.update_to_show="last update on: "+self.current_date[2]+'/'+self.current_date[1]+'/'+self.current_date[0]
        return self.update_to_show


    def init_money(self):
        self.money = Label(self.ws, text="money: ", anchor="w",bg="red", fg="white",bd="10",width=26)
        self.money.place(relx=0.5, rely=0.5, anchor='center')
        return self.money


    def init_money1(self):
        self.money1=ttk.Spinbox(self.ws, width=30, from_=1, to=1000000)
        self.money1.place(relx=0.5, rely=0.6, anchor='center')
        return self.money1

    def init_btn(self):
        self.btn = Button(self.ws, text="Convert",command=self.click,bg="red", fg="white",bd="10",width=26)
        self.btn.place(relx=0.5, rely=0.7, anchor='center')
        return self.btn
    def init_result(self):
        self.ws.result = Label(self.ws, text="result:", anchor="w", bg="red", fg="white",bd="10",width=26)
        self.ws.result.place(relx = 0.5,rely = 0.8,anchor = 'center')
        return  self.ws.result
    def init_last_update(self):
        self.last_update = Label(self.ws, text=self.init_update_to_show(), anchor="w", bg="red", fg="white", bd="10", width=26)
        self.last_update.place(relx=0.5, rely=0.15, anchor='center')
        return self.last_update


# function that keep all the convert in file text
    def keep_all_convert(self,convert_from_txt,convert_to_txt,money_convert,result):
        now = datetime.now()
        today = date.today()
        fdate = date.today().strftime('%d/%m/%Y')
        current_time = now.strftime("%H:%M:%S")
        with open('ConversionDocumentation.txt', 'a') as the_file:
            the_file.write(f'date:{fdate} time: {current_time} from: {convert_from_txt} to: {convert_to_txt} money: {money_convert} result: {result}\n ')

    def init_update(self,temp):
        self.ws.result["text"] = temp

    def click(self):
        if self.money1.get().isdigit():
            print(self.convert_from1.get()+"opo")
            money_convert = int(self.money1.get())
            temp= self.l.convert_from_usd(self.l.convert_to_usd(money_convert, self.convert_from1.get()), self.convert_to1.get())
            self.init_update(temp)
            self.keep_all_convert(self.convert_from1.get(), self.convert_to1.get(), money_convert, temp)
        self.money1.delete(0, END)