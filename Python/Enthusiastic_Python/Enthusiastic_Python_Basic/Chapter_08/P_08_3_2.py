# Enthusiastic_Python_Basic #P_08_3_2

def main():
    for i in range(2, 100):
        if i % 2 == 0 or i % 3 == 0:
            continue
        print(i, end=' ')

main()