# import sys

# print("가", "나", "다", sep="--", end="?")
# print("바보")

# print("python", "java", file=sys.stdout) # 표준 출력
# print("python", "java", file=sys.stderr) # 표준 에러 출력 로깅

# scores = {"수학" : 0, "영어" : 50, "코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(3), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ....
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # 빈공간 채우기

# answer = input("아무 값이나 입력하세요 : ") # input시 항상 str 형식으로 받음.
# answer = 10
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")