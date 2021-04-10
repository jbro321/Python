# Enthusiastic_Python_Basic #P_05_4_2

def show_reverse(rvs):
    for i in range(len(rvs)):
        print(rvs[(i+1)*-1], end=' ')

print(show_reverse([1, 2, 3, 4, 5]))