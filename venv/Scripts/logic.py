
from server import *



from datetime import *

class logic():

    s=server()
    data_json=s.data_json
    # functions to conver
    def convert_to_usd(num,kind):
        print(float(num/float(data_json["rates"][kind])))
        return float(num/float(data_json["rates"][kind]))
    def convert_from_usd(num,kind):
        print(float(num*float(data_json["rates"][kind])))
        return float(num*float(data_json["rates"][kind]))

    # function that keep all the convert in file text
    def keep_all_convert(convert_from_txt,convert_to_txt,money_convert,result):
        now = datetime.now()
        today = date.today()
        fdate = date.today().strftime('%d/%m/%Y')
        current_time = now.strftime("%H:%M:%S")
        with open('ConversionDocumentation.txt', 'a') as the_file:
            the_file.write(f'date:{fdate} time: {current_time} from: {convert_from_txt} to: {convert_to_txt} money: {money_convert} result: {result}\n ')
    def click(self,convert_from1,convert_to1,money1):
        convert_from_txt=(convert_from1.get())
        convert_to_txt=(convert_to1.get())
        if money1.get().isdigit():
            money_convert = int(money1.get())
            print(money_convert,convert_from_txt,convert_to_txt)
            temp=convert_from_usd(convert_to_usd(money_convert,convert_from_txt),convert_to_txt)
            print(temp)
            update(temp)
            keep_all_convert(convert_from_txt,convert_to_txt,money_convert,temp)
        money1.delete(0, END)

    def update(temp):
       ws.result["text"]=temp