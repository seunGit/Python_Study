# # while
# cust = "가나다"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 주문되었어요. {1}번남았어요".format(cust,index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분 되었습니다.")

# # 무한루프
# c = "가나다"
# index = 1
# while True:
#     print("{0}, 커피가 주문되었어요. {1}번남았어요".format(c,index))
#     index+=1

c = "가나다"
person = "Unknown"

while person != c :
    print("{0}, 커피가 주문되었습니다.".format(c))
    person = input("이름이 어떻게 되세요?")