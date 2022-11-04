file = open("../csv/lotto.txt","r", encoding="utf-8")
lines = file.readlines()
file.close()

lotto = []
for i in range(0,5):
    line = lines[i].strip().split(",")
    for j in range(0,len(line)):
        line[j] = int(line[j])
    lotto.append(line)


a = []
for i in range(0,45):
    a.append(0)

for nums in lotto:
    for num in nums:
        a[num-1] = a[num-1]+1

max_num = max(a)
min_num = min(a)
max_nums = []
min_nums = []


for i in range(0,len(a)):
    if a[i] == max_num:
        max_nums.append(i+1)
    elif a[i] == min_num:
        min_nums.append(i+1)


file = open("../csv/ana_lotto.txt","w", encoding="utf-8")
file.write(f"가장 많이 나온 수는{max_nums} {max_num}번 나왔다\n")
file.write(f"가장 많이 나온 수는{min_nums} {min_num}번 나왔다\n")
file.close()



# #처음에 파일에서 데이터를 받아온다
# 내가 필요한 데이터만 만든다
# 카운트를 해야하니까
# 필요 범위까지의 기초 카운트하기 전(0) 리스트를 만들었다
# 내가 필요한 데이터에서 카운트를 했다
# 카운트 한 데이터에서 가장 작은 수 와 가장 큰 수를 구했다
# 그 데이터에 맞는 데이터 리스트를 만들었다
# 파일에 필요한 데이터를 형식에 맞게 써서 저장했다