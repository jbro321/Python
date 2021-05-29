# prints모듈을 위한 파일

def prt1():
    print("I'm Niceboy!")

def prt2():
    print("I'm Goodboy!")

# 단위 실행(독립적으로 파일 실행)
# main이 아니기 때문에 직접 그냥 하면 실행이 안된다.
if __name__ == "__main__":
    prt1()
    prt2()
