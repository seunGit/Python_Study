import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "가나다", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # b 는 binary
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with 사용 - close() 따로 안해줘도 됨.

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
#     # close() 따로 안해도 됨.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요.")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())