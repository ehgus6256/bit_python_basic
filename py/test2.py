#import  가장 위에 입력함
import random
from datetime import datetime
# 0*45 <= 랜덤*45 < 1*45
# print(random.random()*45)   #0~1사이의 랜덤한 수가 나옴
#1~45 숫자 6개
f = open("../csv/lotto.txt","w", encoding="utf-8")
for i in range(0,5):
    lotto = []
    a = []
    while len(lotto) !=6:
        # str(random.random()*45+1).split(".")[0]
        num = int(str(random.random()*45+1).split(".")[0])
        num_pass = True
        for j in lotto:
            if j == num:                
                num_pass = False
                break
        if num_pass:
            lotto.append(num)
    lotto.sort()
    lotto_6 = str(lotto)
    f.write(lotto_6+"\n")
    




# "7.098813057808721".split(".")
# ["7","098813057808721"][0]

# print(datetime.datetime(2022,11,4).today())   #import datetime
f.write(f"출력시간 : {datetime.today()}")     #from datetime import datetime

f.close()

# print(lotto_6)
# int_lotto = int(lotto_6)


def make_six_number():
    lotto = []
    while len(lotto) !=6:
        # str(random.random()*45+1).split(".")[0]
        num = int(str(random.random()*45+1).split(".")[0])
        num_pass = True
        for j in lotto:
            if j == num:                
                num_pass = False
                break
        if num_pass:
            lotto.append(num)
        lotto.sort()
        return lotto
file = open("../csv/lotto.txt","w",encoding="utf-8")
for i in range(0,5):
    lotto = make_six_number()
    for num in lotto:
        file.write(f"{num},")
    file.write("\n")
file.write(f"출력시간:{datetime.today()}")
file.close()