from __future__ import print_function


a = [2,3,4,5,10]
b = [4,5,6,7,8]
set_a = set(a)
set_b = set(b)
x = list(set_a & set_b)
x.sort()
print(x[len(x)-1])



# or



a, b = [2,3,4,5,10], [4,5,6,7,8]
set_a, set_b = set(a), set(b)
x = list(set_a & set_b)
x.sort()
x.reverse()
print(x[0])




# a와b의 교집합중 최댓값 출력하는방법



print