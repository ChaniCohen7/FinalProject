from tkinter import END

from server import *
from datetime import *

class logic():
    def __init__(self):
        self.s=server()
        self.data_json=self.s.data_json
        print(self.data_json)


    # functions to conver
    def convert_to_usd(self,num,kind):
        print(float(num/float(self.data_json["rates"][kind])))
        return float(num/float(self.data_json["rates"][kind]))
    def convert_from_usd(self,num,kind):
        print(float(num*float(self.data_json["rates"][kind])))
        return float(num*float(self.data_json["rates"][kind]))
