# import urllib library
from urllib.request import urlopen
# import json
import json
# import tkinter
import tkinter
from tkinter import *
from datetime import *
from datetime import date


# store the URL in url as
# parameter for urlopen
url = "https://api.exchangerate-api.com/v4/latest/USD"
# store the response of URL
response = urlopen(url)
# storing the JSON response
# from url in data
data_json = json.loads(response.read())
# print the json response
print(data_json)
def convert_to_usd(num,kind):
    print(float(num/float(data_json["rates"][kind])))
    return float(num/float(data_json["rates"][kind]))
# print(convert_to_usd(86,"AED"))
def convert_from_usd(num,kind):
    print(float(num*float(data_json["rates"][kind])))
    return float(num*float(data_json["rates"][kind]))
# print(convert_from_usd(2,"AED"))
def keep_all_convert(convert_from_txt,convert_to_txt,money_convert,result):


    now = datetime.now()
    today = date.today()
    fdate = date.today().strftime('%d/%m/%Y')



    #print("Today's date:", today)
    current_time = now.strftime("%H:%M:%S")
    with open('ConversionDocumentation.txt', 'a') as the_file:
        the_file.write(f'\n date:{fdate} time: {current_time} from: {convert_from_txt} to: {convert_to_txt} money: {money_convert} result: {result}')
def click():
    convert_from_txt=(convert_from1.get(ACTIVE))
    convert_to_txt=(convert_to1.get(ACTIVE))
    money_convert = int(money1.get())
    print(money_convert,convert_from_txt,convert_to_txt)
    money1.delete(0, END)
    temp=convert_from_usd(convert_to_usd(money_convert,convert_from_txt),convert_to_txt)
    print(temp)
    result = Label(f, text=temp, anchor="w", bg="red", fg="blue",bd="10")
    result.pack(fill="x", padx=100, pady=10)
    keep_all_convert(convert_from_txt,convert_to_txt,money_convert,temp)

ws = Tk()
ws.title('Python Guides')
ws.geometry('4000x3000')
ws.config(bg='#1bafb8')
f = Frame(ws,padx=200, pady=80)
convert_from = Label(f, text="convert_from: ", anchor="w",bg="red", fg="blue",bd="10")
convert_from.pack(fill="x",padx=100, pady=10)
convert_from1 = Listbox(f, width=15, height=3, font=("Helvetica", 12))
convert_from1.pack(fill="x")
scrollbar = Scrollbar(f, orient=HORIZONTAL)
scrollbar.pack(fill="x")
convert_from1.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=convert_from1.xview)
convert_to = Label(f, text="convert_to: ", anchor="w",bg="red", fg="blue",bd="10")
convert_to.pack(fill="x" ,padx=100, pady=20)
convert_to1 = Listbox(f, width=15, height=3, font=("Helvetica", 12))
convert_to1.pack(fill="x")
scrollbar = Scrollbar(f, orient=HORIZONTAL)
scrollbar.pack(fill="x")
convert_to1.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=convert_to1.xview)
for x in data_json["rates"].keys():
    convert_from1.insert(END, x)
    convert_to1.insert(END, x)
money = Label(f, text="money: ", anchor="w",bg="red", fg="blue",bd="10")
money.pack(fill="x",padx=100, pady=30)
money1 = Entry(f,width="30")
money1.pack(padx=100, pady=35)
btn = Button(f, text="Convert",command=click,bg="red", fg="blue",bd="10")
btn.pack(fill="x")
f.pack(padx=100, pady=40)
f.mainloop()









