# 카카오 서비스
# 카카오 택시, 카카오 톡, 카카오 페이
# 카카오 로그인(id, password, name)
# 택시 (내위치, 목적지)
# 카카오 톡 (친구) 
# 카카오 페이 (계좌번호, 돈)

# 택시(id, password, name, 내위치, 목적지)

from kakao.kakao_id import kakao_id
from kakao.kakao_pay import kakao_pay
from kakao.kakao_talk import kakao_talk
from kakao.kakao_taxi import kakao_taxi
from kakao.kakao_services import kakao_services


id = kakao_id("id","password","name")

services = kakao_services(id)
a = kakao_taxi("id","password","name","서울","부산")
print(a.목적지)
services.append_service(a)
b = kakao_pay("id","password","name","계좌번호","1000000원")
print(b.돈)
c = kakao_talk("id","password","name","친구")
print(c.친구)
