from random import *

# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

users = range(1, 21) # 1부터 20까지의 숫자를 생성
# users = tuple(users) # () tuple 형식으로 담기
# users = set(users) # {} set 형식으로 담기
users = list(users) # users를 리스트로 담기
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 뽑기
print(winners)

print("-- 당첨자 발표 --")
print("치킨 당점차 :", "{}".format(winners[0]))
print("커피 당첨자 :", "{}".format(winners[1:]))
print("-- 축하합니다. --")