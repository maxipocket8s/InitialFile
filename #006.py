# 함수 정의하기
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money): # balance: 잔액, money: 입금액
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money
balance = 700
balance = deposit(balance, 1000)
balance = deposit(balance, 1500)
deposit(balance, 300) # balance update X
deposit(balance, 500) # balance update X

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money # return: 함수 외부로 반환
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance # return: 명기하지 않으면 함수 외부에서 None 출력된다.

balance = 1000
balance = withdraw(balance, 700)
balance = withdraw(balance, 700)
print(balance)

def withdraw_night(balance, money): # 저녁에 출금, 수수료 발생
    commission = 100 # 수수료 100원
    if balance >= money:
        print("{0}원 출금이 완료되었습니다. 수수료 {1}원이 발생했으며, 잔액은 {2}원입니다.".format(money, commission, balance-money-commission))
        return balance - money - commission
    else:
        print("잔액이 부족합니다.")
        return balance
balance = 3500
balance = withdraw_night(balance, 500)
balance = withdraw_night(balance, 900)

def withdraw_ngt(balance, money):
    commission = 100
    return commission, balance - money - commission
balance = 3500
commission, balance = withdraw_ngt(balance, 1000)
print("수수료 {0}원, 잔액 {1}원입니다.".format(commission, balance))


# 함수 기본값 설정
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 언어: {2}".format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 같은 학년, 같은 반, 같은 수업 >> 기본값 설정한다.
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 언어: {2}".format(name, age, main_lang))
profile("박주원")

def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")


# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") # end = " " >> 줄 바꾸지 않으려고
    print(lang1, lang2, lang3, lang4, lang5)
profile("유재석", 20, "Python", "Java", "Java script", "C", "C++")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # lang1~lang5 모두 기재해야 하므로

def profile(name, age, *language): # *: 가변인자 표시
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
       print(lang, end = " ")
    print() # 줄 바꾸기 위해
profile("유재석", 20, "Python", "Java", "Jave script", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")
