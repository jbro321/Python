# 문제
# ***a,b,c,d 변수 4개를 초기 입력으로 받는다
# *** 출력문 작성 시  a+b를 직접 사용해서 합을 출력하지 않는다.
# *** 아래 출력을 그대로 출력한다. 대신 []안에 내용은 출력하지 않아도 된다.
# *** 수1 + 수2 = 합 문장을 출력하면 된다.

# 출력 
# --------------------
# a[입력받은 값] + b[입력받은값] = 합
# c[입력받은 값] + d[입력받은값] = 합

#1

from datetime import datetime
 
now = datetime.now()
print(now)

import sys

a = list(map(int, sys.stdin.readline().split()))
# a, b, c, d = map(int, input().split())

print("{} + {} = {}".format(a[0], a[1], sum(a[:2])))
print("{} + {} = {}".format(a[2], a[3], sum(a[2:])))

now = datetime.now()
print(now)