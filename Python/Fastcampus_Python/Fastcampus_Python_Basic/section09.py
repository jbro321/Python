# section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
# f = open('./resource/review.txt', 'r')
f = open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f)) # f의 사용법
# 반드시 close 리소스 반환
f.close()

print("----------------------------------------")
print("----------------------------------------")

# 예제2 # with문은 close 생략해도 된다.
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print("----------------------------------------")
print("----------------------------------------")

# 예제 3
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r') as f:
    for c in f: # 1라인씩
        print(c.strip()) # strip은 양쪽 공백을 없애준다. 줄바꿈도 없어진다.

print("----------------------------------------")
print("----------------------------------------")

# 예제 4
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없어서 두번째에서는 아무것도 없다.
    print(">", content)

print("----------------------------------------")
print("----------------------------------------")

# 예제 5
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='#### ')
        line = f.readline() # line별로 읽어온다. 한 문장씩

print("----------------------------------------")
print("----------------------------------------")

# 예제 6
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/review.txt', 'r') as f:
    contents = f.readline()
    print(contents)
    for c in contents:
        print(c, end=' ********* ')

print("----------------------------------------")
print("----------------------------------------")
print()

# 예제 7
score = []
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line)) # txt파일이라 int로 바꿔줘야한다.
    print(score)

print('Average ; {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f) # 파일로 직접 쓴다.
    print('Test Contests2!', file=f)



















