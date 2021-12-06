# 기본 연습하기
print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋ"*9)
print(5>10)
print(5<10)


# T & F
print(not True)
print(not False)
print(not (5>1))


# 애완동물을 소개해주세요.
print("우리 강아지의 이름은 찌개입니다.")
print("찌개는 5살이며, 산책을 아주 좋아해요.")
print("찌개는 어른일까요? True")


# 변수 사용하기
animal = "강아지"
name = "찌개"
age = 5
hobby = "산책"
is_adult = age >= 3

print("우리 " + animal + "의 이름은 " + name + "입니다.")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
# + 기호 대신에 , 쓰면 str 처리하지 않아도 된다.
# 단 , 쓰면 띄어쓰기 되므로 주의한다.
print(name, "는 어른일까요? ", is_adult)


''' 이렇게 하면
여러 문장이 동시에
주석처리가 됩니다. '''

# ctrl + / 누르면 주석처리 가능합니다.


# Quiz) 변수를 이용하여 다음 문장을 출력하시오.
station = "사당"
print(station + "행 열차입니다.")


# 연산하기
print(1+1)
print(2**3) # 2^3 = 8
print(5%3) # 나머지 2
print(10%3) # 1
print(5//3) # 몫 1
print(10//3) # 3
print(4>=7) # False
print(3==3) # True
print(4==2) # False
print(3+4==7) # True
print(1!=3) # True
print(not(1!=3)) # False
print((3>0) and (3<5)) # True
print((3>0) & (3<5)) # True
print((3>0) or (3>5)) # True
print((3<0) | (3>5)) # False


# 수식에 대해
print(2+3*4) # 14
number = 2+3*4 # 14
print(number)
number = number+2 #16
print(number) # 16
number += 2 # 18
print(number) # 18
number /= 2 # 9
print(number)
number %= 2 # 나머지 1
print(number)


# 함수 구하기
print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 최댓값 12
print(min(5, 12)) # 최솟값 5
print(round(3.14)) # 반올림 3
print(round(4.99)) # 반올림 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성

# 정수로 구하려면 int.
print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random()*10)+1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random()*45)+1) # 1 ~ 45 이하의 임의의 값 생성

# 범위로 구하려면 randrange, 마지막 값 포함되지 않는다.
print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하의 임의의 값 생성

# 범위로 구하되, 마지막 값 포함시키려면 randint.
print((randint(1, 45))) # 1 ~ 45 이하의 임의의 값 생성


''' Quiz) 당신은 최근 코딩스터디를 새로 만들었습니다.
월 4회 스터리를 하는데 3번은 온라인, 1번은 오프라인으로 진행하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
조건 1: 랜덤으로 날짜를 뽑아야 함.
조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함.
조건 3: 매월 1~3일은 스터디 준비를 해야하므로 제외함.
출력물 예제_ 오프라인 스터디 모임 날짜는 매월 00일로 선정되었습니다.'''

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")