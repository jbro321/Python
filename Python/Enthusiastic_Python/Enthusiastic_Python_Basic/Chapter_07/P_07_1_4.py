# Enthusiastic_Python_Basic #P_07_1_4

def main():
    num = int(input("num값을 입력하세요: "))
    print("num에 저장된 값은 2의 배수이지만 3의 배수는 아니다. 맞는가?")
    print((num % 2 == 0) and (num % 3 != 0))

print(main())