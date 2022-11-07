from kakao.kakao_id import kakao_id
class kakao_services:
    kakao_id_info :kakao_id |None = None
    service_list = []
    def __init__(self) -> None:
        self.kakao_id_info = _kakao_id
        pass

    def append_service(self,any_service):
        self.service_list.append(any_service)

    def __str__(self) -> str:
        answer = f"""id : {self.kakao_id_info.id}
        ,password : {self.kakao_id_info.password}
        ,service_list : {self.service_list}"""
        return answer