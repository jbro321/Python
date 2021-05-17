# section04_3
# 파이썬데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
# 인덱싱 범위를 지정하는게 슬라이싱 ex) 1:2
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000] # c의 1과 2사이
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()


# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort() # 오름차순
print(y)
y.reverse() # 내림차순
print(y)
y.insert(2, 7)
print(y)
y.remove(2) # 숫자 2를 찾아서 지운다.
y.remove(7)
print(y)
y.pop() # 맨 마지막을 꺼내고 없앤다. 스택이다.
print(y) # LIFO
ex = [88, 77]
y.extend(ex)
print(y)
y.append(ex) # ex가 리스트라서 리스트 자체를 삽입
print(y)

# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

# del c[2] 튜플은 삭제할 수 없다.

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:1])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()
print()
print()

# 튜플 함수

z = (5, 2, 1, 3, 4)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))
