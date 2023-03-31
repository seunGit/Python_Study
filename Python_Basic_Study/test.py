# 문자열 포맷
print("나는 %d살 입니다." % 20)
print("나는 %s살 입니다." % "삼겹")
print("Apple의 앞글자는 %c 입니다." % "A")
print("나는 %s살 입니다." % "100")

print("{}".format(20))
print("{} {}".format(20,"바보"))
print("{1} {0}".format(20,"바보"))

age = 20
color = "빨강색"
print(f"{age}, {color}")

# 탈출문자
print("백문이 불여일견\n백견이 불여일타") # 줄바꿈
print("나는 '바보'입니다.")
print('나는 "바보"입니다.')
print("\"나는 \"바보\"입니다.\"")
print("Users\\seung-gi\\Desktop\\back-end-develop\\python\\test.py")

# \r : 커서를 맨 앞으로 이동 수정
print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭 : 4칸 띄우기
print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] # 0 ~ 5 직전까지
print(my_str)
print(url[7:])
print(url[7:12])
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{},{}".format(url, password))
print(f"{url},{my_str},{password}")