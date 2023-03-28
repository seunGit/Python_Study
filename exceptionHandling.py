# 예외처리 : try - except

# try:
# # 계산기
#     print("나누기 전용 계산기")
#     # num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     # num2 = int(input("두번째 숫자를 입력하세요 : "))
#     nums =[]
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")

# 
class BigNumerError(Exception):
    # pass
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. : "))
    num2 = int(input("첫 번째 숫자를 입력하세요. : "))
    if num1 >= 10 or num2 >=10:
        # 예외 처리 시키기
        raise BigNumerError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
except BigNumerError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
# finally 는 오류가 나든 정상실행되든 상관없이 실행됨. try 뒤에 사용한다.
# 프로그램의 강제종료를 막음으로써 프로그램의 완성도를 높이는데 사용된다.
finally:
    print("계산기를 이용해 주셔서 감사합니다.")