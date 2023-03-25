# # 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# # open_account() # 함수 정의를 해줘야 print문이 실행됨

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money: # 잔액이 출금액보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance
    
# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance -money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))

# def profile(name, age, lang):
#     print("이름 : {0}, 나이 : {1}살, 언어: {2}".format(name, age, lang))

# profile("유재석", 20, "자바")

# 기본값 지정
# def profile(name, age=17, lang="파이썬"):
#     print("이름 : {0}, 나이 : {1}살, 언어: {2}".format(name, age, lang))

# profile("유재석")

# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 {0}, 나이 {1}".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 {0}, 나이 {1}".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "go", "c", "c+", "js")
# profile("김태호", 20, "python", "java", "go")

# 지역변수 : 함수 내에서만 사용 가능 호출 끝나면 사라짐, 전역변수 : 모든 공간에서 부를수 있음
gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용 , 자주 사용안됨
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))