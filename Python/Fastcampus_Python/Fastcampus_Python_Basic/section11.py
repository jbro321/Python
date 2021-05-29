# section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv 이러한 format이다.

import csv

# 예제1
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵할때
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제2
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # 탭이 아닌거로 구분되어 있을 때
    # next(reader) Header 스킵할때
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------------------')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# newline은 줄바꿈을 안하겠다 -> 줄바꿈이 두번되므로
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v) # 하나하나 검증할때는 writerow

# 예제5
with open('C:/Workspace/Python/Python/Fastcampus_Python/Fastcampus_Python_Basic/resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 검증 끝났다면 writerows

# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용(oprnpyxl, xlrd를 내부적으로 사용한다.) 판다스로 만능으로 사용
# pip install xlrd
# pip install openpyxl
# pip install pandas




















