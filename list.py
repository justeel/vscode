
#사전
# cabinet = {3:"김주철" , 4: "맹주혁" , 5: "정승원"}
# print(cabinet[3])
# # 없는 숫자를 적으면 거기서 종료 .get()을 사용하면 none 나옴
# print(cabinet.get(6))
# # print("hi")

# # print(3 in cabinet)
# # print(6 in cabinet)

# # cabinet = {"a-3" : "김주철" ,"b-2" : "엄준식"}
# # print(cabinet)
# # #손님추가
# # cabinet["a-4"] = "박종우"
# # print(cabinet)
# # print(cabinet["a-4"])
# # # 집에간 손님
# # del cabinet["a-3"]
# # print(cabinet)
# # # 사용중인 키 
# # print(cabinet.keys())
# # #벨류 들만 입력 
# # print(cabinet.values())
# # # 키 or 벨류 다 출력
# # print(cabinet.items())

# # # 목욕탕 폐점
# # cabinet.clear()
# # print(cabinet)

# #튜플

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # 튜플은 추가못함

# (name, age, hobby) = ("김주철", 20, "코딩")
# print(name, age, hobby)

# #집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석" , "김주철" , "박명수"}
# python = {"김주철" , "엄준식"}
# # 교집합 자바 파이썬 둘다가능 한사람 찾기
# print(java & python)

# #합집합 java 할 수 있거나 python 할 수 있는 개발자

# print(java | python)

# #차집합 java는 할수있지만 python은 할수없는 사람

# print(java - python)
# print(python - java)

# # python 을 할수있는 사람이 늘어남
# python.add("유재석")
# print(python)
# # 파이썬 까먹음
# python.remove("김주철")
# print(python)

#자료 구조의 변경
# menu = {"커피" , "우유", "주스"}
# print(menu, type(menu)) # set 으로 바꾸기
# menu = list(menu)       #list로 바꾸기
# print(menu, type(menu))
# menu = tuple(menu)      #튜플로 바꾸기
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

from random import*
users = range(1, 21) # 1 ~ 20 숫자 생성
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

win = sample(users, 4)
print(win)
print("---당첨자 발표 ---")
print("치킨 당첨자 :%s" %(win[0]))
print("커피 당첨자 :%s" %(win[1:]))
print(" ---- 축하드립니다 -----")
