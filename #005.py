# if
weather = input("오늘 날씨는 어떠한가요?")
if weather == '비' or weather == '눈':
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 하세요.")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어떠한가요?"))
if temp >= 30:
    print("매우 더우니 야외활동을 자제하세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨입니다.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추우니 야외활동을 자제하세요.")


# for
print("대기번호: 1") # 대기번호: 1
print("대기번호: 2") # 대기번호: 2
for watting_no in [0, 1, 2, 3, 4]:
    print('대기번호: {0}'.format(watting_no))
for watting_num in range(5):
    print('대기번호: {0}'.format(watting_num))

starbucks = ['아이언맨', '토르', '아이엠그루트']
for customer in starbucks:
    print("{0} 님, 커피가 준비되었습니다.".format(customer))


# while
customer = '토르'
index = 5
while index >= 1:
    print("{0} 님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("{0} 님, 커피는 폐기처분 되었습니다.".format(customer))

customer = '아이언맨'
while True:
    print("{0} 님, 커피가 준비되었니다. 호출 {1}회".format(customer, index+1))
    index += 1
    if index == 10: # if 삽입하지 않으면 무한루프
        break

cusomer = '토르'
person = 'Unknown'
while person != customer:
    print('{0} 님, 커피가 준비되었습니다.'.format(customer))
    person = input("성함이 어떻게 되십니까? ") # 조건에 맞지 않으면 while 탈출한다.

# continue
absent = [2, 5] # 결석
sick = [7]
for student in range (1, 11):
    if student in absent:
        continue
    elif student in sick:
        print("{0}번은 보건실에 가고, 오늘 수업은 여기까지.".format(student))
        break # 다음 반복이 있든 없든 반복문을 탈출한다.
    print("{0}번, 발표해보자.".format(student))

# 출석번호 1, 2, 3, 4 >> 101, 102, 103, 104, 105 변경하기
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]

students = ['Iron man', 'Thor', 'I am groot']
print(students)
students = [len(i) for i in students]
print(students) # [8, 4, 10]

students = ['Iron man', 'Thor', 'I am groot']
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']


''' Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때,
총 탑승객 수를 구하는 프로그램을 작성하시오.
조건 1: 승객별 운행 소요시간은 5~50분 사이의 난수로 정해집니다.
조건 2: 당신은 소요시간 5~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 50분)
[O] 3번째 손님 (소요시간: 5분)
...
[O] 50번째 손님 (소요시간: 16분)

총 탑승객 수: 2명'''

# guests = range(1, 51)
# from random import *
# i = 1
# while i <= 50:
#     set(guests)
#     guests[i] = str(randrange(5, 51)) # TypeError: 'range' object does not support item assignment
#     if int(guests.value()) <= 15:
#         print("{O} {0}번째 손님 (소요시간: {1}분)".format(i, guests[i]))
#     else:
#         print("{ } {0}번째 손님 (소요시간: {1}분".format(i, guests[i]))
#     i += 1

from random import *
time = []
cnt = 0
for i in range(0, 50):
    time.append(randrange(5, 51))
    if time[i] <= 15:
        print("[O] {0}번째 손님 (소요시간: {1}분)".format(i+1, time[i]))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i+1, time[i]))
print("총 탑승객 수: {}명".format(cnt))

from random import *
cnt = 0 # 총 탑승객 수
for i in range(1, 51):
    time = randrange(5, 51) # 5~50분 사이 소요시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간: {1}분".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분".format(i, time))
print("총 탑승객 수: {}명".format(cnt))
