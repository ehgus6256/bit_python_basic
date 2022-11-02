#반복문
# for 변수 in 리스트 :
#range(start,stop[, step(뛰는 단위)]) 
# start <= range < stop
# start >= range > stop 도 가능



#a = [5,8,7,9,10]
# print(a[0])
# print(a[1])
# print(a[2])
# i = index
# indexof()
# i 자리에 el = element 로 쓰는 경우도 있다

# for i in range(0,len(a)):
#     if a[i]%2 == 0:
#         print(f"{a[i]}는 짝수입니다")
#     else:
#         print(f"{a[i]}는 홀수입니다")

#for el in a:
#    if el % 2 == 0:
#        print(f"{el}는 짝수입니다")
#    else:
#        print(f"{el}는 홀수입니다")



# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

# for i in range(1,6):
#     print("*"*(6-i))
# for i in range(5,0,-1)
#   print("*"*i)


# person = {"name" : "kim" , "age" : 13}
# person1 = {"name" : "park" , "age" : 15}
# person2 = {"name" : "lee" , "age" : 16}
# a = [person,person1,person2]



# person_excel = [["name","age"],["kim",13],["park",15],["lee",16]]
# keys = person_excel[0]
# datas = person_excel[1:]
# save = []
# # print(data)
# for data in datas:
#     #print(data)
#     tmp = {}
#     for i in range(0,len(keys):
#         tmp[keys[i]] = data[i]
#     save.append(tmp)
# print(save)






# money = 43250
# a = [10000,5000,1000,500,100,50,10]
# for won in a :
#     if money // won >=1:
#         print(f"{won}원 짜리는 {money//won}개 있고")
#         money = money-(money // won)*won
#     else:
#         print(f"{won}원 짜리는 없다")









a = [47,90,1,23,40,5]
count1, count2, count3, count4 = 0, 0, 0, 0
for el in a:
    answer = f"{el}는"
    if el % 2 == 0 and el % 3 == 0:
        answer += "2와 3의 공배수 입니다"
        count1 = count1 +1
    elif el % 2 == 0 or el % 3 == 0:
        if el % 2 == 0:
            answer += "2의 배수 입니다"
            count2 = count2 +1
        elif el % 3 == 0:
            answer += "3의 배수 입니다"
            count3 = count3 +1
    else:
        answer += "2와 3의 공배수가 아닙니다"
        count4 = count4 +1
    print(answer)
print(f"2와 3의 공배수는{count1}개 입니다")
print(f"2의 배수는{count2}개 입니다")
print(f"3의 배수는{count3}개 입니다")
print(f"2와 3의 공배수가 아닌 것은 {count4}개 입니다")




a = [47,90,1,23,40,5]
tmp = {
     0:{"s":"2와 3의 공배수가 아닌것은","count":0}
    ,2:{"s":"2와 3의 공배수가 아닌것은","count":0}
    }

for el in a:
    answer = f"{el}는"
    if el % 2 == 0 and el % 3 == 0:
        answer += "2와 3의 공배수 입니다"
        count1 = count1 +1
    elif el % 2 == 0 or el % 3 == 0:
        if el % 2 == 0:
            answer += "2의 배수 입니다"
            count2 = count2 +1
        elif el % 3 == 0:
            answer += "3의 배수 입니다"
            count3 = count3 +1
    else:
        answer += "2와 3의 공배수가 아닙니다"
        count4 = count4 +1
    print(answer)
print(f"2와 3의 공배수는{count1}개 입니다")
print(f"2의 배수는{count2}개 입니다")
print(f"3의 배수는{count3}개 입니다")
print(f"2와 3의 공배수가 아닌 것은 {count4}개 입니다")

print(f"{tmp.get(0).get('str')}{tmp.get(0).get('count')}개 입니다")




# a = [47,90,1,23,40,5]
# count1 = 0
# count2 = 0
# for el in a:
#     if el % 2 == 1:
#         print(f"{el}는 홀수입니다")
#         count1 = count1+1
#     else:
#         print(f"{el}은 짝수입니다")
#         count2 += 1
# print(f"홀수는 {count1}개 입니다")
# print(f"짝수는 {count2}개 입니다")


