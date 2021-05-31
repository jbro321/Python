# 문제
#    다음 세 가지 중 고르시오.
#    1. 감자. 2.옥수수 3. 수박
#    1번을 누를 시
#    1번 감자를 선택하셨습니다. 라는 문구가 나오도록.
#    2번을 누를 시
#    2번 옥수수를 선택하셨습니다.
#    3번을 누를 시,
#    3번 수박을 선택하셨습니다.
#    >>>>>>>>>>>>>>>>>>>>>>>>>>>>
#    그 뒤 1번 감자에서 1천원어치, 2천원어치 3천원어치.
#    2번을 누를 시 옥수수에서 4천원어치, 5천원어치 6천원어치,
#    3번을 누를 시 수박에서 10000천원어치, 20000천원어치, 30000천원어치.
#    라는 문구가 각각 나오도록 설정하고,
#    그 안에서 또 1번을 누를 시
#    “감자 1천원어치를 선택하셨습니다.” 라는 문구가 나오도록 하고,
#    몇 개를 주문하겠냐고 질문한 뒤 그 개수에 따라 금액이 변동하도록 하시오.

# 감자, 옥수수, 수박 선택

print("안녕하세요! J마켓에 오신 것을 환영합니다!")
print()
print("아래 항목 중에 한가지를 선택해주세요^^")
print("---------------------")
print("1.감자 2.옥수수 3.수박")
print("---------------------")
num = int(input())

if num == 1:
    print("1번 감자를 선택하셨습니다.")
    print("---------------")
    print("얼마치를 선택하시겠습니까?")
    print("1. 1천원어치")
    print("2. 2천원어치")
    print("3. 3천원어치")
    print("---------------")
    price = int(input())
    if price == 1:
        print("감자 1천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 1000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 2:
        print("감자 2천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 2000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 3:
        print("감자 3천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 3000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
elif num == 2:
    print("2번 옥수수를 선택하셨습니다.")
    print("---------------")
    print("얼마치를 선택하시겠습니까?")
    print("1. 4천원어치")
    print("2. 5천원어치")
    print("3. 6천원어치")
    print("---------------")
    price = int(input())
    if price == 1:
        print("옥수수 4천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 4000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 2:
        print("옥수수 5천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 5000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 3:
        print("옥수수 6천원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 6000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
elif num == 3:
    print("3번 수박을 선택하셨습니다.")
    print("---------------")
    print("얼마치를 선택하시겠습니까?")
    print("1. 10000원어치")
    print("2. 20000원어치")
    print("3. 30000원어치")
    print("---------------")
    price = int(input())
    if price == 1:
        print("수박 10000원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 10000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 2:
        print("수박 20000원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 20000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))
    elif price == 3:
        print("수박 30000원어치를 선택하셨습니다.")
        print()
        print("몇 개를 주문하시겠습니까?")
        number = int(input())
        sum = 30000 * number
        print()
        print("총 금액은: {}원 입니다.".format(sum))