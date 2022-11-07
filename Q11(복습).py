# #파이썬
# #특징
# 동적 타이핑(타입을 걸어주지 않아도 알아서 선언 됨)
# a = "code"
# 스크립트 언어(한줄씩 읽어 내려가면서 마지막 선언을 따름)
# a = []
# 문자
# a = "code" 'code'
# 숫자
# a,b = 1,2
# a+b = #3
# () 튜플(읽기 전용)
# {} 딕셔너리
# key : Value
# {"age":20}.get("age")   #20
# set {} 중복불가 순서 없음
# a = {1,2,3}
# a[0]    #set은 순서가 없어서 오류
# [] 리스트
# 순서가 있음
# a = [1,2,3]
# a[0]    #1

# if ~ : 만약에 (조건문)
# 만약 오늘이 일요일이었으면 오늘은 쉴텐데
# today = "월요일"
# if today == "일요일":
#     print("쉰다")
# elif today == "토요일":
#     print("쉰다")
# else :
#     print("출근")

# match today:
#     case "월요일":
#         print("출근")
#     case "일요일":
#         print("쉰다")


# for(반복문)
# 1 <= 변수 < 5
# for 변수 in range(1,5):
#     print(변수)

# a = [1,2,3,4]
# for 변수 in a:
#     print(변수)

# i = 0
# while i < 5:
#     print(i)
#     i += 1


# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 10:
#         break
#     elif i % 3 == 0:
#         continue



# 함수
# def sum(a:int,b:int = 1):    #:int 는 타입 , 1은 기본값
#     return a + b
# try:
#     print(sum(1,2))   #3
# except:
#     print("잘못된 입력값")


# def sum(*a):   # * = 튜플    / 가변적으로 넣을때 많이 사용
#     print(a)
# sum(1,2,3,4,5)   #1,2,3,4,5


# def people(**a):   # ** = 딕셔너리 
#     print(a)
# people(name = "kim" , age = "20")


# print("hi",1,end = "")

# num = input("숫자를 입력하세요")
# print(num)

# open("파일명","w/r/a")


# file = open("test1.txt","w")
# file.write("hi")
# file.close()


# file = open("test1.txt","a")
# file.write("\nappend")
# file.close()


# file = open("test1.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()


# 경로
# 상대경로  test1.txt   # . = 내 위치  /  .. = 내 위치에서 한단계 상위 폴더
# file = open("./test1.txt","r")
# 절대경로  C:\python_q\test1.txt
# file = open("C:\python_q\test1.txt","r")



# import random  #random 의 코딩 파일을 전부 끌고옴 사용할 경우가 적은 문법들을 끌고와서 사용
# print(random.random())


# class
# a = list
# a.append()


# @ 데코레이션(꾸며주는 것)

# print(list(range(10)))  ==  print(list(range(0,10)))

# # @overload
# def sum(a,b):
#     return a+b

# # @overload
# def sum (a):
#     return a

# print(sum(1,2))
