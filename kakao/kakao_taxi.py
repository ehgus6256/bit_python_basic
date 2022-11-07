from kakao.kakao_id import kakao_id

class kakao_taxi(kakao_id):
    내위치 = ""
    목적지 = "" 
    def __init__(self, _id, _password, _name, _내위치, _목적지 ) -> None:
        super().set_id(_id)
        super().set_password(_password)
        super().set_name(_name)
        self.내위치 = _내위치
        self.목적지 = _목적지
        pass

    def 