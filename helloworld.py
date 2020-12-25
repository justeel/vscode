# 처음부터 복습

ani = "강아지"
name = "딸랑이"
age = 2
hobby = "산책"
is_adult = age >= 3

print("우리집" + ani + "의 이름은" + name + "입니다")
print(name + "는" + str(age) + "살 이며," + hobby + "를 좋아합니다")
hobby = "공놀이"
print("생각해보니" + hobby + "를 더 좋아하는거 같아요")
print(name + "는 어른일까요?" +str(is_adult))

station = "홍대입구"
gate = 3
print(station + "행 열차가 " + str(gate) + "번 게이트로 들어오고있습니다")

print (10**9)
print (10%3) 
print (10//3)

print (3==3)
print (2 != 3)
print (not 2!= 3)
print (2 < 3 and 3 < 7)
print (2 > 3 and 2 < 7)
print (2 < 3 or 3 > 5)

number = 2 + 2 * 2
print(number)
number += 2 
print(number)
number *= 2
print(number)
number /= 4
print(number)

# 숫자 처리 함수

print(abs(-5))
print(pow(2, 3))
print(max(1, 100))
print(min(1, 2, 50, 100))
print(round(2.59))

# 추가로 알면좋은것 
from math import*
print(floor(4.99))
print(ceil(4.11))
print(sqrt(16))

#랜덤 함수
from random import*
# print(random() * 100) # 0.0 ~ 100 미만의 값
# print(int(random() * 100)) #소숫점 없이 0 ~ 100 미만의 값
# print(int(random() *3) +1) #1 ~3 까지의 값
# # 예시 로또번호
# print(int(random()*45) +1)  # 1~ 45이하의 임이의 값
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 

print(randrange(1,46)) # 1~ 46 미만의 임의의 값 생성 
print(randint(1, 45)) # randrange 가 헷갈린다 이거사용하면 좋음
 
 #예제 문제
#오프라인 모임날짜 정하기 
# 조건 랜덤 날짜 # 월별 날짜를 다름을 감안하여 최소 28 일로 정함
# 매월 1~3일은 스터디 준비를 해야 하므로 제외
from random import*
date = (randint(4, 28))
print("오프라인 스터디 모임 날짜는 매월"+ str(date) + "로 정해졌습니다")