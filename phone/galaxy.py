from phone.smart_phone import smart_phone

class galaxy(smart_phone):
    sampay = False
    def __init__(self,_name,_price,_sampay = True) -> None:
        super().__init__(_name,_price)
        super().set_name(_name)
        super().set_price(_price)
        self.sampay = _sampay
        pass