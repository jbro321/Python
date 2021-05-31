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
phone text, website text, regdata text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Park', 'Park@naver.com', '010-1234-5678', 'Park.com', ?)", (nowDatetime,))
# ?로 된거는 뒤의 값으로 대체된다.

















