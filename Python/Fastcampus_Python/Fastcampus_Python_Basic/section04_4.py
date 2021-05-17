# section04_4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MangoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-7777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]} # 숫자로 key 설정 잘 안한다.

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3]) # 슬라이싱가능

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

# keys, values, items(key와 value 한쌍)
print(a.keys()) # key만 리스트 형태로 가져온다.
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(list(a.values()))

print(list(a.items()))
print(1 in b)
print(2 in b)
print('name2' not in a)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

# set은 주로 변환해서 사용한다.

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7)

print(s3)

s3.remove(15)
print(s3)

print(type(s3))


