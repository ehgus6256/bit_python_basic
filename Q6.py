#while / match case


# while ~ 동안


# i =0
# while i<5:
#     if i == 3:
#         i +=1
#         continue
#     print(i)
#     i = i+1

#0
#1
#2
#3
#4


# i =0
# while i<5:
#     if i == 3:
#         break
#     print(i)
#     i = i+1

#0
#1
#2


# i = 0
# while True:
#     if i == 60000:
#         break
#     print(i)
#     i +=1

# 0~59999



# a = [0,1,3,5,7,9,10,11,13]

# for i in a:
#     if i % 2 == 1:
#         print(i)

# for i in range(0,len(a)):
#     if a[i] % 2 == 1:
#         print(a[i])


# i = 0
# while i < len(a):
#     if a[i] == 0:
#         print(0)
#     elif a[i] % 2 == 1:
#         print(f"{a[i]} 홀수")
#     elif a[i] % 2 == 0:
#         print(f"{a[i]} 짝수")
#     i += 1


# i = 0
# while i < len(a):
#     if a[i] == 0:
#         i += 1
#         continue

#     if a[i] % 2 == 1:
#         print(f"{a[i]} 홀수")
#     elif a[i] % 2 == 0:
#         print(f"{a[i]} 짝수")
#     i += 1




# match case 매치가 되다 같다
# if 와 비슷함


# i = 0
# while i < len(a):
#     match a[i]%2 :
#         case 1:
#             print(f"{a[i]} 홀수")
#         case 0:
#             print(f"{a[i]} 짝수")
#     i += 1


# i = 0
# while i < len(a):
#     flag = "짝수"
#     if a[i] == 0:
#         i+=1
#         continue
#     if a[i]%2 ==1:
#         flag = "홀수"
#     match flag :
#         case "홀수":
#             print(f"{a[i]} 홀수")
#         case "짝수":
#             print(f"{a[i]} 짝수")
#     i += 1



#람다 (개인적으로 공부) 
# filter - 필터링 
# a = [0,1,3,5,7,9,10,11,13]
# b = [1,3,5,7,9,11,13]
# c = [] #a에 있는 홀수만
# for i in range(0,len(a)):
#     if a[i] % 2 == 1:
#         c.append(a[i]) 
# print(c)


# map - list를 새로운 list로 만든다
# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = []
# for i in range(0,len(a)):
#     c.append(a[i] * 2)
# print(c)


# reduce - 합을 구할때 사용
# a = [0,1,3,5,7,9,10,11,13]
# b = [0,2,6,10,14,18,20,22,26]
# c = 0
# for i in range(0,len(a)):
#     c +=a[i]
# print(c)



#