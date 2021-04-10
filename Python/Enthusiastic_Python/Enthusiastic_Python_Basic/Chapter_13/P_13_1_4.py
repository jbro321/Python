# Enthusiastic_Python_Basic #P_13_1_4

class Friend:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def show_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone)

def main():
    f1 = Friend('윤지민', '010-111-222')
    f2 = Friend('이선준', '010-333-444')
    f3 = Friend('장지우', '010-555-666')
    f4 = Friend('윤지율', '010-777-888')

    frs = [f1, f2, f3, f4]

    for i in frs:
        if i.get_name() == '장지우':
            i.set_phone('010-999-999')

    for i in frs:
        if i.get_name() == '장지우':
            i.show_info()

main()