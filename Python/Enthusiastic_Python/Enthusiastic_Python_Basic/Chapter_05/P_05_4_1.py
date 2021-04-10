# Enthusiastic_Python_Basic #P_05_4_1

def sum_all(sum):
    result = 0
    for i in range(len(sum)):
        result += sum[i]
    return result

print(sum_all([1,2,3,4,5]))