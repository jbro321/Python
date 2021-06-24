# 문제1
# 2~40 단까지 구구단 출력

# 요구사항1) 짝수단만 출력하시오
# 요구사항2) 4,8,12단은 출력하지 마시오
# 요구사항3) 18,20 단은 118단 120단으로 출력되게 하시오
# 요구사항4) 10단 단위마다 한 단계 진행된 단이 출력되게 하시오

# 요구사항4 예시)
# 10단일 경우 11단 출력
# 20단일 경우 21단 출력

for i in range(2, 41, 2): # (start, end, step)

    k = 0

    if (i == 4) or (i == 8) or (i == 12):
        continue
    if (i == 10) or (i == 30) or (i == 40):
        k = i + 1
    if i == 18:
        k = 118
    if i == 20:
        k = 120

    for j in range(1, 10):
        if (i == 10) or (i == 30) or (i == 40):
            print("{} * {} = {}".format(k, j, k*j))
        elif (i == 18) or (i == 20):
            print("{} * {} = {}".format(k, j, k*j))
        else:
            print("{} * {} = {}".format(i, j, i*j))
    print()
