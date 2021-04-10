# Enthusiastic_Python_Basic #P_09_1_1

def to_list(t):
    li = []
    for i in t:
        li.append(i)
    return li

ds = eval(input("입력: "))
ds = to_list(ds)
print(ds)