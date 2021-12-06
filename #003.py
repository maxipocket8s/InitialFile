# 작은 따옴표와 큰 따옴표 사용하기
sentence1 = "나는 소년입니다."
print(sentence1)
sentence2 = '파이썬은 쉬워요.'
print(sentence2)
# 큰 따옴표 세 개 사용하면 줄 바꾸기도 가능하다.
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)


# Slashing
jumin = "940502-2111111"
print("성별: " + jumin[7]) # 2
print("연: " + jumin[0:2]) # 94
print("일: " + jumin[4:6]) # 02
print("생년월일: " + jumin[:6]) # 940502
print("뒤 7자리: " + jumin[7:]) # 2111111
print("뒤 7자리(뒤에서부터): " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 2111111


# str 관련 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # python[0] 문자가 대문자인지? True
print(len(python)) # python 길이(띄어쓰기도 포함) 17
print(python.replace("Python", "Java")) # Python을 Jave로 변경한다.

index = python.index("n") # 'python'에서 'n' 위치를 알려준다.
print(index)
index = python.index("n", index+1) # 두 번째 'n' 위치
print(index)

print(python.find("n"))
print(python.find("Java")) # 원하는 값이 없기 때문에 -1 값이 나온다.
# print(python.index("Java")) # 원하는 값이 없으므로 오류 내며 프로그램을 종료한다.
print(python.count("n")) # 'python'에서의 'n' 개수


# str 포맷
print("a" + "b") # 띄어쓰기 안 되며 ab 나타난다.
print("a", "b") # 띄어쓰기 되며 a b 나타난다.

# 방법 1
print("나는 %d살입니다." % 28) # %d = 정수
print("나는 %s을 좋아합니다." % "파이썬") # %s = 숫자와 문자 모두 가능하다.
print("오늘은 %s월 %s일로, 제 %s입니다." % (5, 2, "생일"))
print("Apple은 %c로 시작해요." % "A") # %c = 문자(한 글자)
print("나는 %s색과 %s색을 좋아합니다." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(28))
print("나는 {}색과 {}색을 좋아합니다.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파란", "빨간")) # 빨간색과 파란색

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 28, color = "빨간"))

# 방법 4
print("당신의 연령은?")
age = input()
print("당신의 취미는?")
hobby = input()
print("당신은 {age}살이며, {hobby}을 즐겨해요.")


# 탈출문자
print("백문이 불여일견 백견이 불여일타")

# \n 줄 바꾸기 위해 사용한다.
print("백문이 불여일견\n백견이 불여일타")

# \', \" : 문장 내 따옴표 역할을 한다.
print("저는 '박주원'입니다.")
print('저는 "박주원"입니다.')
print("저는 \"박주원\"입니다.")

# \\ : 문장 내에서 \
# print("C:\Users\pjw20\OneDrive\바탕 화면\Juwon.py>") # 오류처리
print("C:\\Users\\pjw20\\OneDrive\\바탕 화면\\Juwon.py>")

# \r : 커서를 맨 앞으로 이동한다.
print("Red Apple\rPine") # PineApple

# \b : 백스페이스(한 글자 삭제한다.)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple


''' Quiz) 사이트 별 비밀번호를 만들어주는 프로그램을 작성하시오.
예. http://naver.com
규칙 1. http:// 부분은 제외 >> naver.com
규칙 2. 처음 만나는 점(.) 이후 부분은 제외 >> naver
규칙 3. 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + '!' 로 구성
규칙에 따라 생성된 비밀번호: nav51! '''

URL = input()
a = URL[7:]
print(a)
index = a.index(".")
print(index)
b = a[:int(index)]
print(b)
c = str(b[:3]) + str(len(b)) + str(b.count("e")) + "!"
print(c)

url = input()
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)


# 리스트 []
''' 지하철 칸 별로 10, 20, 30명 탑승 가정하면,
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30] '''

bus = ["유재석", "조세호", "박명수"]
print(bus)

# 조세호 씨가 몇 번째 자리에 앉아 있는지?
print(bus.index("조세호"))

# 다음 정류장에서 하하 씨 탑승함
bus.append("하하")
print(bus) # bus = ["유재석", "조세호", "박명수", "하하"]

# 정형돈 씨를 유재석 씨와 조세호 씨 사이에 앉히자.
bus.insert(1, "정형돈")
print(bus) # bus = ["유재석", "정형돈", "조세호", "박명수", "하하"]

# 끝 사람부터 하차할 때
print(bus.pop()) # 하하
print(bus) # bus = ["유재석", "정형돈", "조세호", "박명수"]

# 동명이인 몇 명인지 확인하기
bus.append("유재석")
print(bus.count("유재석")) # 2

# 정렬도 가능
num_list = [5, 2, 3, 1, 4]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기도 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # []

# 다양한 자료형 함께 사용 가능하다.
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list = [5, 2, 3, 1, 4]
num_list.extend(mix_list)
print(num_list) # [5, 2, 3, 1, 4, "조세호", 20, True]