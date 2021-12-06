'''Quiz) 동네에 항상 대기 손님이 있는 맛집 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하여 예외처리 구문을 넣으시오.

조건1: 1보다 작거나, 또는 숫자가 아닌 입력값이 들어오면 ValueError로 처리한다.
        출력 메시지: "잘못된 값을 입력하였습니다."
조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정한다.
        치킨 소진 시 사용자 정의 에러[SoldOutError]로 프로그램 종료시킨다.
        출력 메시지: "재고가 소진되어 주문을 받지 않습니다."

[코드]
chicken = 10
waiting = 1 # 홀은 만석, 대기번호 1부터 시작한다.
while(True):
    print("[남은 치킨: {}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken:
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1
        chicken -= order'''

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    try:
        print("[남은 치킨: {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <= 0 :
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
              raise SoldOutError("재고가 소진되어 주문을 받지 않습니다.")
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break
    