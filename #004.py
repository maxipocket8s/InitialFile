# 사전 기능
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
print(cabinet.get(3)) # 유재석

# print(cabinet[5]) # 오류 발생 후 프로그램 종료
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용가능")) # 5 값이 있으면 값을 출력하나, 값 없을 시 '사용가능' 출력한다.

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# 새로운 손님
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국" # 유재석에서 김종국으로 교체된다.
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])
# value만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])
# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])
# 목욕탕 폐점
cabinet.clear()
print(cabinet) # {}


# 튜플 기능
# 내용 변경 불가하나 속도가 빠르다.
menu = ("돈까스", "생선까스")
print(menu[0]) # 돈까스

name = "박주원"
age = 28
hobby = "코딩"
print(name, age, hobby) # 박주원 28 코딩
(name, age, hobby) = ("박주원", 28, "코딩")
print(name, age, hobby) # 박주원 28 코딩


# 세트(집합) 기능
# 중복 불가하며 순서가 없다.
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])
# 교집합(java와 python 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
# print(java and python) 불가 # and: 비교연산자라 조건문에서 사용한다.
print(java.intersection(python)) # {'유재석'}

# 합집합(java와 python 중 하나라도 할 수 있는 개발자)
print(java | python)
# print(java or python) 불가 # or: 비교연산자라 조건문에서 사용한다.
print(java.union(python))

# 차집합(java 할 줄 아나 python 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# 추가 및 제거
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}
java.remove("김태호")
print(java)


# 자료구조 변경
M0 = {"커피", "우유", "주스"}
print(M0, type(M0)) # {'커피', '우유', '주스'} <class 'set'>
M1 = list(M0) # 리스트로 만들기
print(M1, type(M1)) # ['커피', '우유', '주스'] <class 'list'>
M2 = tuple(M1) # 튜플로 만들기
print(M2, type(M2)) # ('커피', '우유', '주스') <class 'tuple'>
M3 = set(M2) # 다시 세트로 만들기
print(M3, type(M3)) # {'커피', '우유', '주스'} <class 'set'>


'''
Quiz) 당신의 학교에서 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
댓글 작성자 중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1: 댓글 작성자는 20명이고, 아이디는 1~20이다.
조건 2: 댓글 내용과 무관하게 추첨하되 중복은 안 된다.
조건 3: random 모듈의 shuffle과 sample을 활용한다.

(출력예제)
-- 당첨자 발표 --
치킨 당첨자: 3
커피 당첨자: [5, 17, 20]
-- 축하합니다. --
'''

from random import *
event = []
for i in range (0, 10):
    event.insert(i, randrange(1, 21))
    if(len(set(event)) == 4):
        break
print("-- 당첨자 발표 --")
chicken = event[0]
print("치킨 당첨자: ", chicken)
event = set(event)
event.remove(chicken)
print("커피 당첨자: ", event)
print("-- 축하합니다. --")

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(x)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자: ", sample(x, 1))
# print("커피 당첨자: ", sample(x, 3))
# print("-- 축하합니다. --")
# 중복 출력 가능성 있기 때문에 실패한 코딩

users = range(1, 21) # 1부터 20까지 숫자를 생성한다.
print(type(users)) # range
users = list(users)
print(users)
shuffle(users)
print(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("-- 축하합니다. --")