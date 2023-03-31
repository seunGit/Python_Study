# 50명의 승객

# 조건1 : 승객별 운행 소요시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

from random import *

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1~50 수 (승객)
    time = randrange(5, 51) # 5분~ 50분 소요시간
    if 5 <= time <=15: # 5분 ~ 15분 이내 손님, 탑승 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("==================================")
print()
print("총 탑승 승객 : {0}분 ".format(cnt))