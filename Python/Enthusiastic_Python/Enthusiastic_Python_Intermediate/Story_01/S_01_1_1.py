# Enthusiastic_Python_Intermediate #S_01_1_1

# rc(reference count)는 객체를 참조하는 변수의 수

r1 = [1, 2, 3] # [1, 2, 3]의 rc = 1 ( [1, 2, 3]은 r1 참조 )
r2 = r1 # [1, 2, 3]의 rc = 2 ( [1, 2, 3]은 r1와 r2 참조 )
r1 = 'simple' # [1, 2, 3]의 rc = 1 ( [1, 2, 3]은 r2 참조 )
r2 = 'happy' # [1, 2, 3]의 rc = 0 ( [1, 2, 3]은 참조 없음, 따라서 가비지 컬랙션)