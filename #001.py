print('hello!') # 작은 따옴표 안에 문자를 입력하면 그대로 출력된다.
print("I'm Juwon") # 큰 따옴표 안에 문자를 입력하면 그대로 출력된다.
print("%d" % 10) # "%d" 정수를 의미한다.
print("%d / %d = %d" % (20, 10, 2)) # 큰 따옴표 안에 수식 형식을 지정하여 입력할 수 있다.
print("%d / %d = %1.1f" % (10, 20, 0.5)) # 실수를 출력하려면 %0.1f 형식으로 입력한다.
print("hello"[0:2]) # he
print("hello"[2:5]) # llo


# 조건문 사용하기
a=10
if(a==20):
    print("ten")
else:
    print("?")

b=20
if(b<=10):
    print("10보다 작다.")
else:
    print("10보다 크다.")

no = input()
if(int(no) % 2 == 0):
    print("짝수")
else:
    print("홀수")

yes = input()
if(int(yes) > 27):
    print("늙은이네..")
elif(int(yes) == 27):
    print("하이루 친구!")
else:
    print("나보다 어리잖아?")

what = input()
if(int(what) % 4 == 0):
    print("spring")
elif(int(what) % 4 == 1):
    print("summer")
elif(int(what) % 4 == 2):
    print("fall")
else:
    print("winter")

x = input()
if(x == 1):
    print("one")
elif(x == 2):
    print("two")
elif(x == 3):
    print("three")
else:
    print("wrong number")