# 사용자로부터 숫자를 입력받아
# 이 숫자가 홀수인지 짝수인지 판별하세요.

# 얼마? 151
# 151은 홀수입니다.

data = input("얼마?    : ")

if int(data)%2:
    print(data, "는 홀수입니다.")
else:
    print(data, "는 짝수입니다.")