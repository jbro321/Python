# section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3 # 기본적으로 패키지에 포함되어 있다.
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

# sqlite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMBERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, \
phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Park', 'Park@naver.com', '010-1234-5678', 'Park.com', ?)", (nowDatetime,))
# ?로 된거는 뒤의 값으로 대체된다.
# Primary key는 중복이 되면 안되서 에러가 난다.
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)",  (2, 'LEE', 'LEE@naver.com', '010-0000-0000', 'Lee.com', nowDatetime))

# Many 삽입(튜플, 리스트) 한번에 삽입 - 웹에서 크롤링 등 해온 데이터를 한번에 등록
userList = (
    (3, 'Kim', 'kim@naver.com', '010-2222-2222', 'Kim.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(오토 커밋)
# conn.commit() 을 해야 반영된다.
# 커밋 롤백은 시점이 중요하다.

# 롤백
# conn.rollback()

# 접속 해제
conn.close()






