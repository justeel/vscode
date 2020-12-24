print("필생즉사 \n필사즉생")


# 저는 "김주철" 입니다 .
# print("저는 \"김주철\" 입니다.")

# \r : 커서를 맨 앞으로 이동 


print("red apple\rpine")

# \b : 백스페이스 (한 글자 삭제)
print("redd\bAplle")

#\t : 탭
print("red \t apple5")

url = "http://naver.com"
my_str = url.replace("http://", "") # replace = 바꾸는거
print(my_str)
my_str = my_str[:my_str.index(".")] 
#index . < . 전까지만 출력 0~ 5 직전까지
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀 번호는 {1} 입니다 ". format(url, password))