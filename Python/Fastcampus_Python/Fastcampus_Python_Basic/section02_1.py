# section02_1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용

print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me')) #순번대로 맵핑
print("{a} are {b}".format(a='You', b='Me'))

 # %s : 문자, %d : 정수, %f : 실수
print("%s's foavorite number is %d" % ('JP', 7))

print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) # %4.2f는 정수부분 4자리, 실수부분 2자리
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123)) # {0: 5d}는 0번째는 5d이다
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

print("'you'")
print("\'you\'")
print('"you"')
print("""'you'""")
print('\\you\\\n\n\n\n')
print('\t\t\ttest')
