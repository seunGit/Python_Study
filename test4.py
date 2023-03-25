# 튜플 - 내용변경 추가가 안됨. 속도가 리스트보다 빠르다.

menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# menu.add("생선가스") # 추가 안됨

name = "가나다"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("가나다", 20, "코딩")
print(name, age, hobby)