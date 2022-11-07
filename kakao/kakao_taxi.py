from kakao.kakao_id import kakao_id

class kakao_taxi(kakao_id):
    내위치 = ""
    목적지 = "" 
    def __init__(self, _id, _password, _name, _내위치, _목적지 ) -> None:
        super().__init__(_id, _password, _name, _내위치, _목적지)