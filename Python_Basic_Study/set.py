# 집합 (set)
# 중복안됨, 순서없음
my_set = {1, 2, 3, 3}
print(my_set) # 중복 값 없이 1,2,3만 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 모두 할수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python 할수있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java 할수잇지만 python 할수 없는 개발자)
print(java - python)
print(java.difference(python))

# python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)

# -----------------------------------------------------------------

# 자료구조의 변경

menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# -----------------------------------------------------------------
