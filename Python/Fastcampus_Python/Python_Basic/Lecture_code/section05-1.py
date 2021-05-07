# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습


print(type(True))
print(type(False))

# 기본 형식

# 예1
if True:
    print("Yes")  # 들여쓰기 중요

if False:
    # 출력되지 않음.
    print("No")

# 예2
if False:
    # 여기는 실행되지 않음.
    print("You can't reach here")
else:
    # 여기가 실행된다.
    print("Oh, you are here")

# 관계연산자
# >, >=, <, <=, ==, !=


a = 10
b = 0

# == 양 변이 같을 때 참.
print(a == b)

# != 양 변이 다를 때 참.
print(a != b)

# > 왼쪽이 클때 참.
print(a > b)

# >= 왼쪽이 크거나 같을 때 참.
print(a >= b)

# < 오른쪽이 클 때 참.
print(a < b)

# <= 오른쪽이 크거나 같을 때 참.
print(a <= b)

# 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None

city = ""
if city:
    print("You are in:", city)
else:
    # 이쪽이 출력된다.
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    # 이쪽이 출력된다.
    print("Please enter your city")

# 논리연산자
# and, or, not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)  # a > b > c
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 3 + 12 > 7 + 3)
print('ex2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('ex3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('ex4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다.")

id1 = "gold"
id2 = "admin"
grade = 'super'

if id1 == "gold" or id2 == "admin":
    print("관리자 로그인 성공")

if id2 == "admin" and grade == "super":
    print("최고 관리자 로그인 성공")

is_work = False

if not is_work:
    print("is work!")

# 다중 조건문
num = 90

if num >= 70:
    print("num ? ", num)
elif num >= 60:
    print("num ? ", num)
else:
    print("default num")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")

# in, not in

q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색
