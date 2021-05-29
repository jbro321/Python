# section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 해준다.

## SyntaxError : 잘못된 문법

# print('Test)
# if True
#     pass
# x => y

## NameError : 참조변수 없음

a = 10
b = 15

# print(c)

## ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

## IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) # 예외 발생

# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month()) # time. 을 누르면 알려준다.





















