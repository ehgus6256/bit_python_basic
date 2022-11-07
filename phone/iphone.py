from smart_phone import smart_phone
# import smart_phone
# smart_phone.smart_phone()
# 상속


class iphone(smart_phone):
    apppay = False
    def __init__(self,_name,_price,_apppay) -> None:
        self.apppay = _apppay
        super().__init__(_name,_price)
        super().set_name(_name)
        super().set_price(_price)
        pass