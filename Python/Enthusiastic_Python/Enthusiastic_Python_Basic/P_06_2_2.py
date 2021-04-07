# Enthusiastic_Python_Basic #P_06_2_2

def birth_only(num):
    num1 = num.split('-')
    num2 = num1[0]
    return num2

""" <모법 답안>
def birth_only(pn):
    ret = pn.split('-')
    return ret[0]
 """

p1 = "070609-2011xxx"
p1 = birth_only(p1)
print(p1)

p2 = "070609-2011xxx"
p2 = birth_only(p2)
print(p2)