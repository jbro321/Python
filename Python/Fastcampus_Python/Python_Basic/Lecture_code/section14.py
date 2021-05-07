# Section14
# 주소록 제작
# 부록 소스 파일

import os.path
# 파일 저장
import pickle


# 연락처 클래스
class Contact:
    def __init__(self, name, phone_num, email):
        self.name = name
        self.phone_num = phone_num
        self.email = email

    # 개인 연락처 출력
    def prt_info(self):
        print("Name : {}".format(self.name))
        print("Phone_number : {}".format(self.phone_num))
        print("e_mail : {}".format(self.email))
        print("-" * 20)
        print()


# 연락처 정보 입력
def add_cont(c_list):
    name = input_name()
    phone_num = input_phone()
    email = input_email()
    print()

    for v in c_list:
        # 같은 이름은 등록 불가능(프로그램 상에서만)
        if name == v.name:
            print('Name exists.')
            print()
            break
    else:
        # 인스턴스 생성
        cont = Contact(name, phone_num, email)
        print('saved.')
        print()
        # 인스턴스 반환
        c_list.append(cont)


# 메뉴 출력
def prt_menu():
    print("1. Add")
    print("2. Info")
    print("3. Delete")
    print("4. DB Save")
    print("5. DB Drop")
    print("6. Exit")
    print()
    # 메뉴 넘버 입력
    menu = input("Select Menu Number : ")
    print()
    return int(menu)


# 이름으로 조회 된 연락처 삭제
def del_cont(c_list):
    # 삭제 할 이름 입력
    nm = input("Name: ")
    print()

    if len(c_list) > 0:
        # enumerate : 인덱스 생성
        for i, cont in enumerate(c_list):
            if str(cont.name).strip() == nm.strip():
                print('"{}" deleted.'.format(cont.name))
                print()
                del c_list[i]  # 해당 리스트 삭제
                break
        else:
            # 삭제 할 데이터 없을 경우
            print('No files to delete.')
            print()
    else:
        # 연락처 리스트가 비어 있을 경우
        print('No files to delete.')
        print()


# 저장 된 모든 연락처 정보 출력
def prt_cont(c_list):
    # 연락처 리스트가 비어 있지 않은 경우
    if len(c_list) > 0:
        # 리스트 형태로 된 인스턴스 정보 출력
        for i in c_list:
            i.prt_info()
    else:
        # 연락처가 비어 있을 경우
        print('Contact is empty.')
        print()


# 파일로 저장
def store_cont_db(c_list):
    try:
        # 기존 DB 있으면 생성, 없으면 추가(Binary)
        with open("cont_db.bin", "wb") as f:
            # pickle 파일로 저장
            pickle.dump(c_list, f)

            print('db saved')
            print()
    except IOError as log:
        print(log)


# 파일 DB 로드
def load_cont_db():
    # pickle 데이터 저장 변수
    p_list = []
    # 파일이 존재하는지 체크
    if os.path.isfile('cont_db.bin'):
        # 예외처리
        try:
            with open("cont_db.bin", "rb") as f:
                p_list = pickle.load(f)
        except IOError as log:
            print(log)
    else:
        # 처음 실행 시 파일이 존재하지 않으면 출력
        print('DB File not found!')
        print()

    return p_list


# 파일 DB 삭제
def drop_cont_db():
    if os.path.isfile('cont_db.bin'):
        # 예외처리
        try:
            # 파일 삭제
            os.remove('cont_db.bin')
            print('DB File dropped.')
        except FileNotFoundError as log:
            print(log)
    else:
        # 파일이 존재하지 않으면 출력
        print('DB File not found!')
        print()


# 이름 입력
def input_name():
    while True:
        try:
            # input() 함수 : 입력 함수(자료형은 무조건 Str)
            name = input("Name: ")
            if len(name) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Name is too short.")
    return name


# 전화번호 입력
def input_phone():
    while True:
        try:
            # input() 함수 : 입력 함수(자료형은 무조건 Str)
            phone_num = input("Phone number: ")
            if len(phone_num) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Phone number is too short.")
    return phone_num


# 전화번호 입력
def input_email():
    while True:
        try:
            # input() 함수 : 입력 함수(자료형은 무조건 Str)
            phone_email = input("E-mail: ")
            if len(phone_email) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Email is too short.")
    return phone_email


# 프로그램 시작
def main():
    # 연락처 리스트 로드
    c_list = load_cont_db()

    while True:
        # 실행 메뉴 번호 저장
        menu = prt_menu()
        if menu == 1:  # 추가
            add_cont(c_list)
        elif menu == 2:  # 출력
            prt_cont(c_list)
        elif menu == 3:  # 삭제
            del_cont(c_list)
        elif menu == 4:  # DB 저장
            store_cont_db(c_list)
        elif menu == 5:  # DB 삭제
            drop_cont_db()
        else:
            break


if __name__ == "__main__":
    # 프로그램 시작
    main()
