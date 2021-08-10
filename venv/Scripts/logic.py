
from server import *
s=server()
data_json=s.data_json
class logic():
    def __init__(self,num,kind):
        self._num=num
        self._kind=kind

    def convert_to_usd(self):
        print(float(_num/float(data_json["rates"][_kind])))
        return float(_num/float(data_json["rates"][_kind]))