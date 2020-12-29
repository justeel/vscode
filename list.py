#리스트
subway = [10 , 20 , 30]
print(subway)
 
subway = ["유재석", "조세호","박명수"]
print(subway) 

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

subway.insert(1 , "정형돈")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

ad = ["조세호", 20 , True]
ad.extend(num_list)
print(ad)
for i in range(1, 101):
    if i % 2  == 0:
        print("good")
    else:
        print(i)
    
