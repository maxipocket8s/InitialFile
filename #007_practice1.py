# pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장한다.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러온다.
print(profile)
profile_file.close()


# with # 자동으로 파일 닫힘
import pickle
with open("profile.pickle", "rb") as profile_file: # profile.pickle 내용을 profile_file 변수로 저장한다.
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부합니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


''' Quiz) 당신은 회사에서 매주 1회 보고서를 작성해야 합니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- O주차 주간보고 -
부서:
이름:
업무 요약:

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건: 파일명은 '1주차.txt'와 같이 만듭니다.'''

i = 1
while i <= 50:
    with open("{0}주차.txt".format(i), "w", encoding='utf8') as file:
        file.write("""
        - {0}주차 주간보고 -
        부서:
        이름:
        업무 요약:
        """.format(i))
    i += 1

for i in range(1, 51):
    with open(str(i)+'주차.txt', "w", encoding="utf8") as report_file:
        report_file.write("-{0}주차 주간보고-".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")