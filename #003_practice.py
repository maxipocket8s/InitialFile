print("안녕하세요,\n주원이의 다이어리에 접근하셨습니다.\n접근 권한이 있는지 확인하겠습니다.\n성함과 연령을 차례대로 기입하시기 바랍니다.")
# print("성함: ")
name = input('성함: ')
# print("연령: ")
age = input("연령: ")
print()
print("당신은 {0}이며 {1}세입니다.".format(name, age))
print()
# import sys
if(name == "전영준" and age == "29"):
    print("환영합니다, 전영준 님.\n보안이 해제되었습니다.")
    answer = input('''
전영준 님은 주원이와의 시간이 너무 좋아서
로또에 당첨되기를 원합니다. 그렇죠?\n('네/아니요'로 대답하세요.) ''')
    from random import *
    if(answer == "네"):
        print("\n그렇다면 주원이가 금주의 당첨 번호를 줄 테니\n부디 잘 받아 적으시기 바랍니다.")
        # while True:
        #    lotto = randrange(1, 46)
        #    lotto_list = []
        #    lotto_list.append(lotto)
        #    lotto_num = set(lotto_list)
        #    if (len(list(lotto_num)) == 7):
        #         break
        # print(lotto_num)
        lotto_num = []
        for i in range(0, 45, 1):
            lotto_num.append(randrange(1, 46))
            if(len(list(set(lotto_num))) == 7):
                break
        print()
        print(set(lotto_num))
    else:
        print("앗, 주원이는 원하는 줄 알았는데.. 슬퍼...")
    print()
    print("오늘은 피곤하니 '쎄구빠'해요!\n다음에 더 재미나게 보여드립죠^^")
    # A = input("종료하시겠습니까?('네/아니요'로 대답하세요.) ")
    # if(A == "아니요"):
    #     print("더 무엇을 하시려고?")
    # else:
    #     sys.exit()
elif(name == "전영준" and age != "29"):
    print("\"뭐하냐?\"\n신분 도용은 범죄입니다.")
    # A = input("종료하시겠습니까?('네/아니요'로 대답하세요.) ")
    # if(A == "아니요"):
    #     print("더 무엇을 하시려고?")
    # else:
    #     sys.exit()
elif(name == "박주원" and age == "28"):
    print("\"나를 기만하다니!\"\n괘씸하니 시스템을 종료합니다.")
    # A = input("종료하시겠습니까?('네/아니요'로 대답하세요.) ")
    # if(A == "아니요"):
    #     print("더 무엇을 하시려고?")
    # else:
    #     sys.exit()
else:
    print("당신에게 접근 권한이 없습니다.\n시스템을 종료합니다.")
    # A = input("종료하시겠습니까?('네/아니요'로 대답하세요.) ")
    # if(A == "아니요"):
    #     print("더 무엇을 하시려고?")
    # else:
    #     sys.exit()
print()
print("안녕히 가십시오.")