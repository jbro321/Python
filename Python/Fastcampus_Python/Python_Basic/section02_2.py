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
    print('Ok') # indent도 문법이다

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# 변수 선언(한글)

이름 = "좋은사람"

# 출력
print(이름)

# 함수 선언

def 인사():
    print("안녕하세요. 반갑습니다.")

인사()

def greeting():
    print('Hello!')

greeting()

# 클래스
class Cookie(): # class Cookie: 괄호 없어도 가능하다.
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))