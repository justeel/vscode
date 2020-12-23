# 슬라이싱
joochul = "971211-1234567"

print("성별 : " + joochul[7])
print("연 : " + joochul[:2])
print("생년월일 :" + joochul[:6])

print("뒤 7자리" + joochul[7:])
print("뒤 7자리 (뒤부터)" +joochul[-7:])

# 문자열 처리함수
python = " naver "
print(python.lower())
print(python.upper())
print(python.replace("naver","google"))

index = python.index("n")
print(index)
print(python.find("google"))
#문자열 포맷
# print("나는 %d살 입니다" % 24) 
# print("나는 %s을 좋아해요"  % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨강"))
print("나는 {}살 입니다" .format(24))
print("나는 {1}색과 {0}색을 좋아해요.)" .format("빨간", "파란"))
print("나는 {a}살이며, {c}색을 좋아해요." .format(a = 24, c = "분홍"))

a = 24
c = "분홍"
print(f"나는 {a}살이며, {c}색을 좋아해요.")

# 줄바꿈
print("필사즉생 \n필생즉사 ")