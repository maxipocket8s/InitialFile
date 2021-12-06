# 표준 입출력
print("Python", "Java") # Python Java
print("Python", "Java", sep=", ") # Python, Java
print("Python", "Java", "C", sep=" vs ") # Python vs Java vs C
print("Python", "Java", sep=", ", end="? ") # end: 줄 바꾸기 대신 "?"으로 출력, 따라서 다음 문장이 이어 나온다.
print("무엇이 더 재밌을까요?") # Python, Java? 무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준오류

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=": ") # 네 칸의 공간을 확보하여 좌우로 정렬한다.

# 은행 대기순번표 001 002 003...
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3)) # 세 칸의 공간을 확보하되 없으면 0으로 채운다.

answer = input("아무 값이나 입력하세요: ") # answer type: str, input = str type
print("입력하신 값은 " + answer + "입니다.")

print("{0: >10}".format(500)) # 오른쪽 정렬을 하되 빈 자리는 빈 공간으로 둔 채 총 10자리 공간을 확보한다.
print("{0: >+10}".format(500)) # 양수일 때 +로, 음수일 때 -로 표시한다.
print("{0:_<+10}".format(500)) # 왼쪽 정렬을 하되 빈 자리는 _로 채운 채 양수일 때 +로, 음수일 때 -로 표시하며 총 10자리 공간을 확보한다.
print("{0:,}".format(10000000000)) # 3자리마다 , 찍어주기
print("{0:+,}".format(10000000000)) # 3자리마다 , 찍으면서 부호 붙이기
print("{0:^<+10,}".format(28)) # 빈 자리는 ^로 채우면서 왼쪽 정렬로 10자리 확보하고, 부호 붙인 채 출력하되 3자리마다 , 표시한다.
print("{0:f}".format(5/3)) # 소수점 출력
print("{0:.2f}".format(5/3)) # 소수점 셋째 자리에서 반올림한다.


# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # 파일명 "score.txt" 용도 "w" writing > 쓰기 기능(혹은 덮어쓰기 기능)
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # 용도 "a" appending > 이어쓰기 기능
score_file.write("과학: 80") # 줄 바꾸기 기능 없다.
score_file.write("\n코딩: 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 용도 "r" reading > 읽기 기능
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽은 후 커서는 다음 줄로 이동한다.
print(score_file.readline(), end="") # 줄별로 읽되 다음 줄로 이동하지 않음. end 이용해서.
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

