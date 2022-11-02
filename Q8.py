# 함수
# def sum(a,b):   #매개 변수
#     print(a)
#     print(b)
#     return a+b

# print(sum(1,2))   #1,2 = 인수



# def sum(a:int,b:int):
#     try:   #시도
#         return a+b
#     except:     #예외
#         return "잘못된 값입니다"
# print(sum(1,4))
# print(sum("hi",4))  




# def diff(a:int,b:int):
#     return a - b
#     if a-b<= 0:      #return을 했기때문에 함수가 끝나서 받을수없음
#         return 0
# print(diff(1,4))



# def diff(a:int,b:int):
#     answer = ""
#     try:
#         dif = a - b
#         if dif < 0:
#             answer = 0
#         else:
#             answer = dif
#     except:
#         answer = "잘못된 값"
#     finally:
#         return answer

# print(diff(1,4))
# print(diff(7,4))
# print(diff("hi",4))
# print(diff(diff(5,3),diff(4,2)))
#1



# def filtering(a):
#     c = []
#     for i in range(0,len(a)):
#         if a[i]  %  2 ==1:
#             c.append(a[i])
#     return c

# list1 = [0,1,3,5,7,9,10,11,13]
# list2 = [13,9,2,22,4,5,65,32]
# list3 = [90,23,4,634,12,43,82]
# print(filtering(list1))
# print(filtering(list2))
# print(filtering(list3))



# def sum(*nums):  # *은 몇개인지 모를 다수를 입력할때 사용(튜플(읽기전용)로 받겠다)
#     answer = 0
#     for num in nums:
#         answer = answer + num
#     return answer

# print(sum(1,2,3,4,5,6))
# print(sum(5,6,7))



# def make_profile(**a):    # **는 key:value 로 받겠다
#     print(a)
#     return

# print(make_profile(name = "park", age = 20, company = 'naver'))

# # {'name': 'park', 'age': 20, 'company': 'naver'}



#함수를 정의할땐 def 이름(매개변수):
#print("hi")도 함수의 종류이며 이때 "hi"는 인수이다
#def print(st):
#def print(*st)     *type(st) = tuple(읽기전용)
#print("hi", "hello", 1,2,3)
#def print)(**st)    *type(st) = dictionary
#print(name = "kim", age = 20)