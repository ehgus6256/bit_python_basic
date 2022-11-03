# while 반복문
# ran = []
# i = 0
# while i < 5 :
#     ran.append(i)
#     i = i+1
# print(ran)
# range(0,5)  # [0,1,2,3,4]


# for j in ran:
#     print(j)

# k = 0
# while True:
#     q = 0
#     while q<10:
#         if k % 2 == 1:
#             k += 1
#             continue
#         elif k == 100:
#             break
#         print("q",q)
#         q+=1
#     print("k",k)
#     k+=1


# 리스트 내부 순서 바꾸기 (정렬)  .sort()


# p = [1,3,2,4]
# tmp = p[1]
# p[1] = p[2]
# p[2] = tmp
# print(p)   #[1,2,3,4]


# p = [1,3,2,4]
# p[1],p[2] = p[2],p[1]
# print(p)   #[1,2,3,4]


# p = [1,2,3,4]
# for i in range(0,len(p)):
#     num_max = p[i]
#     for j in range(i+1,len(p)):
#         if num_max < p[j]:
#             num_max = p[j]
#             p[i],p[j] = p[j],p[i]
# print(p)


# p = [1,2,3,4]
# p_len = len(p)
# o = []
# for i in range(0,p_len):
#     p_max = max(p)
#     o.append(p_max)
#     p.remove(p_max)
# print(o)



# def sum(a,b):
#     try:       #예외처리
#         return a+b
#     except:
#         return "잘못된 값"
# print(sum(1,2))   #3
# print(sum("hi",3))   #잘못된 값



#재귀함수(내가 나를 불러오는 함수)
# def diff(a,b):
#     if a-b ==1:
#         return [a,b]
#     else:
#         return diff(a-b,b)

# print(diff(100,1))



p = [1,2,3,4,5,6]
# p_len = len(p)
# o = []
# for i in range(0,p_len):
#     p_max = max(p)
#     o.append(p_max)
#     p.remove(p_max)
# print(o)


# i = 0
# for i in range(0,len(p)):
#     def sort1(p[i],p[i+1]):
#         if p[i] < p[i+1]:
#             return(p[i+1],p[i])
#         else:
#             return(p[i],p[i+1])
# print (p)


# # target_list = []
# # return_list = []
# def sort1(target_list:list, return_list:list):
#     if(len(target_list)==0):
#         return return_list
#     p_max = max(target_list)
#     return_list.append(p_max)
#     target_list.remove(p_max)
#     return sort1(target_list, return_list)
# print(sort1(p,[]))



# def sum_func(*nums):   #tuple
#     i = 0
#     for num in nums:
#         i += num
#     return i

# print(sum_func(1,2,3,4))    #10
# print(sum_func(1,2,3,4,7,8,9,1))     #35
# print(sum_func(1))    #1


# def person(**info):     #dictionary
#     return info

# print(person(name = "park"))    #{'name': 'park'}



# def person(a,*nums,**info):
#     print(a)
#     print(nums)
#     return info

# print(person("dd",1,2,3,name="park"))
# #dd
# #(1,2,3)
# #{'name': 'park'}



#스플릿
a = "a b c"

# def space_to_list(st:str):
#     b = []
#     for i in st:
#         if i != " ":
#             b.append(i)
#     return b


# print(space_to_list(a))    #['a','b','c']



b = a.split(" ")   #split("")  = ""안의 것을 쉼표로 바꿈
print(b)


