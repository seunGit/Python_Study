absent = [2, 5] # 결석
nobook = [7] # 책을 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in nobook:
        print("오늘수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책 읽어봐".format(student))