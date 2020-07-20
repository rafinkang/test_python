# 숫자를 입력 받아 2로 나눈 나머지를 출력
# 100
# 나머지 0

# input1 = int(input("숫자를 입력하세요."))

# print(input1, "/ 2 =", input1/2, "나머지 = ", input1%2)

# x, y = input("두개의 숫자를 입력하세요").split()
# print('x', x, 'y', y)

# 사용자로부터 국어, 영어, 수학 점수를 입력받아 총점과 평균을 출력
# 90 80 70
# 국어:90 영어:80 수학:70 
# 총점:000 평균:000

kor, eng, mat = input("국어 영어 수학 점수를 입력하세요.").split()
kor, eng, mat = int(kor), int(eng), int(mat)
print("국어 :", kor, "영어 :", eng, "수학 :", mat)
print("총점 :", kor+eng+mat, "평균", (kor+eng+mat)/3)
