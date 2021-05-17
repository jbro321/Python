# section05_3

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리핸션
numbers2 = [x for x in range(1, 101)]
print(numbers2)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.

q3 = ["갑", "정", "병", "을"]

q5 = [x for x in q3 if x != '정']
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

q6 = [x for x in range(1, 101) if x % 2 != 0]
print(q6)

# 문법 설명 x = [x for x in range(1, 100) if 조건문]