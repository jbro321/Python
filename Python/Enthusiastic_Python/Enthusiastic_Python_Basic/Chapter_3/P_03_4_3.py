# Enthusiastic_Python_Basic #P_03_4_3

def exp(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

print(exp(2,3))