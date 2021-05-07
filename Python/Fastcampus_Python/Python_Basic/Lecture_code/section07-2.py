# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        # print('Car Class "Show" Method!')
        return 'Car Class "Show" Method!'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        super().show()
        return 'Car Info : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # Super
print(model1.type)  # Super
print(model1.car_name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub

# Method Overriding
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info
print('Inheritance Info : ', BmwCar.mro())
print('Inheritance Info : ', BenzCar.mro())


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())