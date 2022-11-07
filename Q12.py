# class 계산기:
#     def __init__(self, num = 0):
#         self.num = num

#     def sum(self,a):
#         self.num = self.num + a
#     def diff(self,a):
#         self.num = self.num - a


#     # def diff(self,a):
#     #     return a


# # print(a.sum(1,2))
# # print(a.diff(3,2))


# a = 계산기(1)
# a.sum(1)
# print(a.num)   # 2


# b = 계산기(2)
# b.sum(1)
# print(b.num)   # 3


# c = 계산기()
# print(c.num)


# num = 0   #전역 변수
# def sum(a):
#     num = num + a   #지역 변수
#     print(num)

# sum(1)




# class 이름:
#     def __init__(self) -> None:
#         self.name = "없음"
#     def setname(self, name):
#         self.name = name

# a = 이름()
# print(a.name)
# a.setname("park")
# print(a.name)


# class 사람:
#     name = ""
#     age = 0
#     def __init__(self,_name,_age) -> None:
#         self.name = _name
#         self.age = _age
#     def print_name(self):
#         print(self.name)
#     def print_age(self):
#         print(self.age)

# kim = 사람("kim",30)
# lee = 사람("lee",20)
# print(kim.name)
# print(kim.age)
# print(lee.name)
# print(lee.age)

# #객체지향
# kim = {"name":"kim","age":30}
# kim.get("name")    #  == print(kim.name)
# kim.get("age")     #  == print(kim.age)


# 사람 = {"name":"kim","12843581":"19847824"}    #보장이 안되며 안정성이 떨어짐




# class 숫자:
#     count = 0
#     num1 = 0
#     def __init__(self, _num1) -> None:
#         self.num1 = _num1
#         숫자.count = 숫자.count + 1
# num_list = []
# for i in range(10):
#     num_list.append(숫자(i))
# print(num_list)
# for i in range(10):
#     print(num_list[i].num1)
# print(f"count{num_list[0].count}")


class 랭지:
    ran = []
    def __init__(self, _end):
        i = 0
        while i < _end:
            self.ran.append(i)
            i = i + 1
        

print(랭지(10).ran)

# class  =  객체 지향(oop)