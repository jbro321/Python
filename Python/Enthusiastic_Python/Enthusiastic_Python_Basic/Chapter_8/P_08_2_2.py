# Enthusiastic_Python_Basic #P_08_2_2

def main():
    gcm = 42
    while True:
        if 42 % gcm == 0 and 120 % gcm == 0:
            return gcm
            break
        gcm-=1

print("42와 120의 최대공약수:", main(), end=' ')