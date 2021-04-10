# Enthusiastic_Python_Basic #E_14_1_1

def main():
    bread = 10
    try:
        people = int(input("몇 명? "))
        print("1인당 빵의 수: ", bread/people)
        print("맛있게 드세요.")
    except:
        print("뭔지는 몰라도 예외가 발생했군요.")

main()