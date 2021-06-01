# section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/database.db') # 본인 DB 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())

# print('All -> \n', c.fetchall()) # 커서가 다 가져와져서 빈 리스트만 출력된다.

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회2 (주로 이 방법을 많이 쓰인다.)
# for row in c.fetchall():
    # print('retrieve2 > ', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    # print('retrieve3 > ', row)

print()

# WHERE Retrieve1 # 튜플
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 데이터 없음

# WHERE Retrieve2 # 인테져
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 데이터 없음

# WHERE Retrieve3 # 딕셔너리
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall()) # 데이터 없음

# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3, 4))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())

# Dump 출력
with conn:
    with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() 는 with문에 의해 호출이 되었다.