ain = "앵무새"
hob = "부리쪼기"
name = "로이더"
age = "4"
print(name + "는" +hob+ "를 좋아합니다")
print(name + "는"  +str(age)+ "살 입니다")

from random import*

date = randint(4, 28)
time = randint(17, 24)
print ("우리가 게임하는 시간은" + str(date) + "일" +str(time)+ "시입니다")

sentence = """안녕하세요 저는 김주철 입니다
저는 서울특별시 양천구에서 살고있고 축구를 좋아합니다 """
print(sentence)

joochul = "971211-1234567"

print("성별 :" + joochul[0])
print("연 : " +joochul[0:6])
print("월 : " +joochul[2:6])
print("주민번호 앞자리" + joochul[0:6])
joochul2 = "1111111111111111111111111112111111"
print("테스트 :" + joochul2[:30])
print("테스토 " + joochul2[-10:])

ad = "python is Amazing"
print(ad.lower())
print(ad.upper())
print(ad.replace("python" , "java"))
print(ad)

index = ad.index("n")
print(index)