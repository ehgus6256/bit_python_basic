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



def sum(a,b):
    return a+b

sum(b = 1, a = 2)   # 순서를 바꾸고 싶을때


def sum(a=0,b=0,c=0,type="sum"):
    if type =="sum":
        return a+b+c
    else:
        return a-b-c

print(sum(a=1,b=2,type="sum"))   # 3
print(sum(a=1,b=2,type="ss"))   # -1