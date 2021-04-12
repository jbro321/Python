# Enthusiastic_Python_Intermediate #S_02_1_1

# 리스트는 주소값이 동일하다.
r = [1, 2]
print(id(r)) 
r += [3, 4]
print(id(r))

# 튜플은 주소값이 바뀐다. (새로운 튜플 생성)
t = (1, 2)
print(id(t))
t += (3, 4) # 새로운 튜플이 만들어진다.
print(id(t))

# 성격에 따라 달라지는 함수의 정의
def add_last(m, n):
    m += n

r = [1, 2]
add_last(r, [3, 4]) # r = [1, 2, 3, 4]

t = (1, 3)
add_last(r, (3, 4)) # t = (1, 3)
# t가 참조하는 튜플과 m이 참조하는 튜플은 별개의 것이 된다.

def add_tuple(t1, t2):
    t1 += t2
    return t1 #새로 만들어진 튜플 반환

# 원본의 저장 순서
def min_max(d):
    d.sort()
    print(d[0], d[-1], sep=', ')

l = [3, 1, 5, 4]
min_max(l) # 1, 5
print(l) # [1, 3, 4, 5]

def min_max2(d):
    d = list(d)
    d.sort()
    print(d[0], d[-1], sep=', ')

l = [3, 1, 5, 4]
min_max2(l) # 1, 5
print(l) # [3, 1, 5, 4]