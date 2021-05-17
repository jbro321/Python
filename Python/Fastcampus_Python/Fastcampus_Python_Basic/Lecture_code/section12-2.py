# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('본인이 원하는 경로/database.db')  # 본인 DB 파일 경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 된다.
# 1개 로우 선택
print('One -> \n', c.fetchone())

# 지정 로우 선택
print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
print('All -> \n', c.fetchall())

print()

# 순회1
rows = c.fetchall()
for row in rows:
    print('retrieve1  >', row)  # 조회 없음

# 순회2
for row in c.fetchall():
    print('retrieve2 >', row)  # 조회 없음

# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    with open('본인이 원하는 경로/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')
