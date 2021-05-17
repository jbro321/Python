# section07_2
# 파이썬 클래스 상속 이해
# 상속, 다중상속

# Example 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tuple
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self):  # -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_mode(self):  # -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self): # 부모한테도 있는 메소드
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color) 

# 일반 사용
model1 = BMWCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BenzCar("220d", "Suv", "black")
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info(상속 정보)
print(BMWCar.mro()) # 소스 파악할 때 사용
print(BenzCar.mro())

# Example 2
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