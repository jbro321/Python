# Enthusiastic_Python_Basic #P_07_2_1

def main():
    num = input("정수를 입력하세요: ")
    if num.isdigit():
        print(int(num) ** 2)
    else:
        print("정수가 아닙니다.")

print(main())