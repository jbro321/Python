# Enthusiastic_Python_Basic #P_08_2_1

def main():
    lcm = 1
    while True:
        lcm+1
        if lcm % 6 == 0 and lcm % 45 == 0:
            print("6과 45의 최소공배수", lcm, end = ' ')
            break

print(main())