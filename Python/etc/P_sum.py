# 문제
# ***a,b,c,d 변수 4개를 초기 입력으로 받는다
# *** 출력문 작성 시  a+b를 직접 사용해서 합을 출력하지 않는다.
# *** 아래 출력을 그대로 출력한다. 대신 []안에 내용은 출력하지 않아도 된다.
# *** 수1 + 수2 = 합 문장을 출력하면 된다.

# 출력 
# --------------------
# a[입력받은 값] + b[입력받은값] = 합
# c[입력받은 값] + d[입력받은값] = 합

import sys

a, b, c, d = map(int, sys.stdin.readline().split())
# a, b, c, d = map(int, input().split())

sum1 = a + b
sum2 = c + d

print("{} + {} = {}".format(a, b, sum1))
print("{} + {} = {}".format(c, d, sum2))