# Enthusiastic_Python_Basic #P_12_1_3

dc ={'새우깡': 700, '콘치즈': 850, '꼬깔콘': 750}

dc['홈런볼'] = 900

for i in dc:
    dc[i] += 100

del dc['콘치즈']
dc['치즈콘'] = 950

print(dc)