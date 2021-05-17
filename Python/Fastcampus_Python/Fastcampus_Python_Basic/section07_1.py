# section07_1
# 파이썬 클래스 상세이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#    함수
#    함수
#    함수

# Example 1
# 클래스 네이밍은 주로 첫글자 대문자, 단어단어 연결도 대문자
# 속성(컬러 등), 메소드(누르다, 펜을 갈다 등)
class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)

# 네임스페이스
user1 = UserInfo("Kim")
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1)) # id는 메모리 주소값 출력
print(id(user2)) # id값이 다르다
print(user1.__dict__) # 네임스페이스 출력
print(user2.__dict__)

# Example 2
# self의 이해

class SelfTest(): # 괄호 있어도 되고 없어도 된다.
    def function1():
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

self_test = SelfTest()
# self_test.function()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# Example 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee') # 클래스 네임스페이스, 클래스 변수(공유)

print(WareHouse.__dict__)
print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 자기네임스페이스에 없으면 클래스 네임스페이스에서 찾는다.

del user1

print(user2.stock_num)
print(user3.stock_num)




