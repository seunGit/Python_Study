queue = [4, 5, 6]
queue.append(7)
queue.append(8)
print(queue) # 4, 5, 6, 7, 8

queue.pop()
queue.pop()
print(queue) # 6, 7, 8

list = [4, 5, 6]
list.append(7)
list.append(8)
print(list)

list.pop()
list.pop()
print(list)

cabinet = {3:"가", 100:"나"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) # 값이 없을때 None 출력
print(cabinet.get(5, "사용가능")) # 값이 없을때 None 대신에 사용가능 출력됨
# print(cabinet[5]) # 오류

print(3 in cabinet) # 3 이라는 키값이 cabinet 에 있는지 , True 반환
print(5 in cabinet) # 5 라는 키값이 cabinet 에 있는지 , False 반환

# 새로운 값 입력
print(cabinet)
cabinet["101"] = "다"
cabinet[100] = "라"
print(cabinet)

# 값 삭제
del cabinet[100]
print(cabinet)

# key 값만 출력하기
print(cabinet.keys())

# value 값만 출력하기
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())
print(cabinet)

# 클리어
cabinet.clear()
print(cabinet)