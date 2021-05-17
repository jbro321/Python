# section04_2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy." # 이렇게 str 선언을 더 많이 한다.
str2 = 'NiceMan'
str3 = ''
str4 = str('ace')

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin' # escape없이 출력이 된다.
# raw_s1 = r"" 로 큰 따옴표도 가능하다.
print(raw_s1)

# 멀티라인
# \ 를 적으면 코드가 쭉 이어진다
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman" # 한번 할당되면 바꿀 수 없다. 따라서 반복문 가능

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3) # print(str_o1 + 3) +는안된다.
print('a' in  str_o4) # str_o4에 a가 있는지 묻는 코드이다.
print('f' in  str_o4)
print('z' not in  str_o4)

# 문자열 형 변환
print(str(77) + 'a') # 77을 문자로 인식해서 77a가 출력된다.
print(str(10.4))

# 문자열 함수
# 참고 : 사이트 ~

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(a.endswith('s')) # 문자 안에 들어 있는지 확인하는 함수
# print(a.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(list(reversed(b))) # 리스트처리해야 거꾸로 출력된다.

a = 'niceman' # 한번 선언하면 바꿀 수 없다. immutable
b = 'orange'

print(a[0:3]) # nic 출력
print(a[0:4])
print(a[0:7])
print(a[0:len(a)-1])
print(a[:4]) # 앞은 처음부터라서 생략 가능하다.
print(a[:])
print(b[0:4:2]) # 2개씩 점핑
print(b[1:-2])
print(b[::-1])
