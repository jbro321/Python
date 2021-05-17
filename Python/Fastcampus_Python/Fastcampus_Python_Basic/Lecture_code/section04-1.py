# Section04-1
# 파이썬 데이터 타입(자료형)
# 데이터타입, 숫자형, 숫자형 연산

'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

bytearray
byte
frozenset
'''

# 데이터 타입(Data Type)
v_str1 = "NiceMan"
v_bool = True
v_str2 = "GoodBoy"
v_float = 10.0
v_int = 7
v_list = [v_str1, v_str2]
v_dict = {
    "name": "niceman",
    "age": 25
}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 데이터 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))

# Numeric Operation (숫자형 연산자)
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print("##### + #####")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 
print("i1 + f1 : ", i1 + f1)  # 실수와 정수끼리

# -
print("##### - #####")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)
print("i1 - f1: ", i1 - f1)

# *
print("##### * #####")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)
print("i1 * f1: ", i1 * f1)

# /
print("##### / #####")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)
print("i1 / f1: ", i1 / f1)
print("f1 / i1: ", f1 / i1)

# //
print("##### // #####")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)
print("i1 // f1: ", i1 // f1)
print("f1 // i1: ", f1 // i1)

# %
print("##### % #####")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)
print("i1 % f1 :", i1 % f1)
print("f1 % i1 :", f1 % i1)

# **
print("##### ** #####")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)
print("i1 ** f1: ", i1 ** f1)
print("f1 ** i1: ", f1 ** i1)

# 형 변환 실습
a = 5.
b = 4
c = .4
d = 7.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수
print(int(True))  # Bool -> 정수
print(float(True))  # Bool -> 정수
print(int(False))  # Bool -> 정수
print(float(False))  # Bool -> 정수
print(complex(3))  # 정수 -> 복소수
print(complex('3'))  # 문자 -> 복소수
print(complex(False))  # Bool -> 복소수

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))

#외부 모듈
import math

#ceil
print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))

#floor
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))

#pi
print(math.pi)

# 그 밖에 함수는 아래 URL 참조
# https://docs.python.org/3/library/math.html


# 2진수 변환
print(bin(50)) #0b로 시작
