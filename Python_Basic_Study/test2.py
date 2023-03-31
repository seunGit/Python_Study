subway = ["가", "나", "다"]
print(subway)

# 나 는 몇번째 칸에 타고있나요?
print(subway.index("나"))

# 인원추가
subway.append("라")
print(subway)

# 가와 나 사이에 마 넣기
subway.insert(1, "마")
print(subway)

# 뒤에서 부터 꺼내기
print(subway.pop())
print(subway)

# 중복된 값 확인하기
subway.append("가")
print(subway)
print(subway.count("가"))

# 정렬하기
nl = [5,3,2,1,6]
nl.sort()
print(nl)

# 순서 뒤집기
nl.reverse()
print(nl)

# 모두 지우기
nl.clear()
print(nl)

# 다양하게 자료형 함께 사용
num = [4, 6, 7, 8, 1]
mix = ["가나다", 20, True]
print(mix)

# 리스트 확장
mix.extend(num)
print(mix)