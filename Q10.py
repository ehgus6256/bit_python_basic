#(클래스 class) (oop(rograming) 객체지향)
# a = []

# class = 여러개의 기능을 가지고 있는 것
# python 에선 @ = 데코레이션
# @ overload
# overload = 하나의 이름으로 변수에 따라 기능이 달라질 수 있다


# @overload
# def sum(a:int):
#     return a

# @overload
# def sum(a:str):
#     return a


# print(sum(1))
# print(sum("hi"))

# default 기본값

# print({"name":"kim"}.get("age"))  # -> None
# print({"name":"kim"}.get("age","없어"))  #-> 없어

# print({"name":"kim"}.get("name"))  # -> kim


# @final  -> 수정할수없는 class
# ex range

# range(start, stop, [, step])
# @overload
# def range(start, end):
#     i = start
#     a = []
#     while i != end:
#         a.append(i)
#         i += 1
#     return a
#overload
# def range(start, end, step = 1):
#     i = start
#     a = []
#     while i != end:
#         a.append(i)
#         i += step
#     return a
# print(range(0,10,))   #[0,1,2,3,4,5,6,7,8,9]
# print(range(0, 10 ,2))   #[0,2,4,6,8]



# dict.get()
# list.remove()
# list.append()
# # list = []



# input / open


# input  입력받기
# num = input("숫자를\t입력해주세요\n")   #1
# num1 = input("숫자를\t입력해주세요\n")   #2
# print("print",int(num)+int(num1))
# num+num1 -> "1"+"2" -> "12"
# int(num)+int(num1) -> 1+2 -> 3
# while True:
#     num = input()



# open 파일 오픈
# open -> 쓰고, 읽고, 저장



# def sum(a,b):
#     return a+b

# sum(b = 1, a = 2)   # 순서를 바꾸고 싶을때


# def sum(a=0,b=0,c=0,type="sum"):
#     if type =="sum":
#         return a+b+c
#     else:
#         return a-b-c

# print(sum(a=1,b=2,type="sum"))   # 3
# print(sum(a=1,b=2,type="ss"))   # -1



# open

# f = open("test.txt","w")
# a = []
# for i in range(0,10):
#     a.append(input("입력 : \n"))   # a.write(input("입력": \n")+"\n")
# for el in a:                      #for el in a:
#     f.write(el+"\n")              #f.write(el+"\n") 





# for i in range(0,10):
#     f.write(f"{str(i)}\n")
# f.close()



# f = open("test.txt","w")
# #input("입력:\n") ->end
# #끝나게

# for i in range(0,10):
#     st = input("입력:\n")
#     if st == "end":
#         break
#     f.write(st +"\n")
# f.close()



# f = open("test.txt","r")
# while True:
#     #str == ""    -> False
#     st = f.readline()
#     if st =="":
#         break
#     else:
#         print(st.strip())      #.strip = whitespace(tab,enter)를 지워준다
# f.close()


# f = open("test.txt","r")
# for line in f.readlines():
#     print(line.strip())
# f.close()

# print("ddd\n".strip())
# print("ddd\n")




#연결해서 쓰는거
#csv에서 데이터 만드는거 해보기


#연결해서 쓰기
# f = open("test.txt","w",encoding="utf-8")   #utf-8 = 한글
# f.write("글을 쓴다\n")
# f.close()

# f = open("test.txt","a",encoding="utf-8")   #mode a(append) = 글을 추가
# f.write("글을 쓴다2")
# f.close()



# open의 모드는 w(write),r(read),a(append)
# 한글이 깨지면 encoding = "utf-8" 을 써서 인코딩해라
# 마지막엔 f.close()로 파일을 닫아라



# {"name":"kim","age":15}
# f = open("9898.csv","r", encoding = "utf-8")
# total_data = f.readlines()
# data_keys = total_data[0].strip().split(",")
# data1 = total_data[1].strip().split(",")
# dict1 = {data_keys[0]:data1[0], data_keys[1]:data1[1]}
# print(dict1)
# total_data[2]
# # 'park,18\n' strip -> 'park,18'
# # 'park,18' split(",") -> ['park','18']
# data2 = total_data[2].strip().split(",")
# dict2 = {data_keys[0]:data1[0], data_keys[1]:data1[1]}
# print(dict2)
# f.close()


# .(현위치)/csv(folder)/9898.csv(file)
# ./csv/9898.csv
f = open("./csv/9898.csv","r", encoding = "utf-8")
total_data = f.readlines()
data_keys = total_data[0].strip().split(",")
data_list = []
for i in range(1,len(total_data)):
    data1 = total_data[i].strip().split(",")
    dict1 = {}
    for j in range(0,len(data1)):
        dict1[data_keys[j]] = data1[j]

    # dict1 = {data_keys[0]:data1[0], data_keys[1]:data1[1]}
    # print(dict1)
    data_list.append(dict1)
# print(data_list)
# # total_data[2]
# # 'park,18\n' strip -> 'park,18'
# # 'park,18' split(",") -> ['park','18']
# data2 = total_data[2].strip().split(",")
# dict2 = {data_keys[0]:data1[0], data_keys[1]:data1[1]}
# print(dict2)
f.close()




# 각 사람들의 price 평균을 구하고 price가 평균보다 높은 사람 찾기

# f = open("./csv/9898.csv","r", encoding = "utf-8")
# price_a = []
# price = f.readlines()
# for i in range(0,len(price),3):
#     price1 = price(i)
#     price_a.append(price1)

# price_f = sum(price_a)

# print(price_f)


# price 평균보다 높은 사람들 뽑아내기
# 다 더한거 구하기
# total_sum = 0
# for data in data_list:
#     total_sum += int(data.get("price"))
# price_avg = total_sum/len(data_list)  #평균 구하기
# #평균 이상인 것을 구하기
# answer = []
# for data in data_list :
#     if  int(data.get("price")) > price_avg:
#         answer.append(data)
#     else:
#         continue
# print(answer)



#데이터 뽑아오기
def make_data(file_name:str,mode:str):
    f = open(file_name,mode, encoding = "utf-8")
    total_data = f.readlines()
    data_keys = total_data[0].strip().split(",")
    data_list = []
    for i in range(1,len(total_data)):
        data1 = total_data[i].strip().split(",")
        dict1 = {}
        for j in range(0,len(data1)):
            dict1[data_keys[j]] = data1[j]
        data_list.append(dict1)
    f.close
    return data_list
#평균 구하기
make_data("../csv/9898.csv","r")
def make_data_avg(data_list:list,key:str):
    total_sum = 0
    for data in data_list:
        total_sum += int(data.get(key))
    price_avg = total_sum/len(data_list)
    return price_avg
make_data_avg(make_data("../csv/9898.csv","r"),"price")
#평균 이상인 것 구하기
def answer_avg_high(data_list:list,key:str,price_avg:int):
    answer = []
    for data in data_list:
        if int(data.get("price")) > price_avg:
            answer.append(data)
    return answer
print(answer_avg_high(
    make_data("../csv/9898.csv","r"),
    "price",
    make_data_avg(
        make_data("../csv/9898.csv","r"),
        price_avg)
    ))

