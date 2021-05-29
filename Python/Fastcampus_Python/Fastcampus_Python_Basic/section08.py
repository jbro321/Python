# section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용2(클래스) - 권장하진 않는다.
from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스) - 권장
from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수) - 
from pkg.calculations import div as d
print("ex5 : ", int(d(100, 10)))

# 사용6
import pkg.prints as p
# import builtins 이미 들어있는 함수들
p.prt1()
p.prt2()
# print(dir(builtins))


