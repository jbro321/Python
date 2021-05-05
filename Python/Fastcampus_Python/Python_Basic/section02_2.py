# section02_2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My name is Goodboy!')

# 변수 선언
myName = 'Goodboy'

# 조건문
if myName == "Goodboy":
    print('Ok')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)