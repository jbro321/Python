BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdata text);
INSERT INTO "users" VALUES(1,'Park','Park@naver.com','010-1234-5678','Park.com','2021-06-01 00:39:39');
INSERT INTO "users" VALUES(2,'LEE','LEE@naver.com','010-0000-0000','Lee.com','2021-06-01 00:39:39');
INSERT INTO "users" VALUES(3,'Kim','kim@naver.com','010-2222-2222','Kim.com','2021-06-01 00:39:39');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2021-06-01 00:39:39');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2021-06-01 00:39:39');
COMMIT;
