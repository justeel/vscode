# joochul = "971211-1234567"

# print("성별 : " + joochul[7])
# print("생년월일 : " + joochul[:6] )

# ani = "앵무새는 새야"
# # print(ani.replace("귀여워","이뻐"))

# index = ani.index("새",)
# print(index)
# index = ani.index("새",index + 1)
# print(index)
# print(ani.count("새"))

# print("나는 %d살 입니다" %24)
# print("나는 %s을 좋아해요" %"abc")
# print("나는 %s로 시작해요" % "A")

# print("나는 %s 색과 %s 색을 좋아해요" %("파란","빨간"))

# print("나는 {}살 입니다" .format(20))
# print("나는 {1}색과 {0}을 좋아합니다" .format("파랑" , "빨간"))

# print("나는 {1}살이고 {0}색을 좋아합니다".format("20" ,"빨간"))

# age = 24
# clor = "파랑"
# print(f"나는 {age}살이고 {clor}색을 좋아합니다")

# print("백문이 불여일견 \n백견이 불여일타")
# print('저는 "김주철" 입니다')
# print("저는 \"사람\" 입니다")
# print("자세한 내용은 여기서 확인E:\\vscode\\vscode>")

# print("apple \t am")

a = "http://youtube.com"
b = a.replace("http://", "")
print(b)
b = b[:5]
print(b)
password = b[:3] + str(len(b)) + str(b.count("e")) + "!"
print(password)
print ("%s 의 비밀번호는 %s 입니다" % (b, password))