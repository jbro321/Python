# Section04-2
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

# 문자열 생성
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# 탭, 줄바꿈
t_s1 = "Tab \tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('x' in str_o1)
print('i' in str_o1)
print('e' not in str_o2)
print('O' not in str_o2)

# 문자열 형 변환
print(str(77))  # type 확인
print(str(10.4))
print(str(True))
print(str(complex(12)))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('Nice', 'Good'))
print("replace2: ", str_o3.replace("is", "was", 3))
print("split: ", str_o4.split(' '))  # Type 확인
print("sorted: ", sorted(str_o1))  # reverse=True
print("reversed1: ", reversed(str_o2)) #list 형 변환
print("reversed2: ", list(reversed(str_o2)))

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

# im_str[0] = "T"  # 수정 불가(immutable)

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))
print(chr(116))
