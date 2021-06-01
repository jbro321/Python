# section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/database.db') # 본인 DB 경로

# Cursor 연결
c = conn.cursor()

# 데이터 수정1 # 유닛키 id를 가져와서 바꾸는게 좋다
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

# 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {"name" : 'goodman', "id" : 5})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 3))

# conn.commit() 해야 db에 반영된다.

# 중간 데이터 확인1

# for user in c.execute("SELECT * FROM users"):
#     print(user)

# Row Delete1
# c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
# c.execute("DELETE FROM users WHERE id = :id", {"id" : 5})

# Row Delete3
# c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# 중간 데이터 확인2

for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, "rows")

# 커밋
conn.commit()

# 접속 해제
conn.close() # with문을 안써서 close해줘야한다.
