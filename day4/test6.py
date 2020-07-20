# 사용자로 부터 국어, 영어, 수학 점수를 입력받는다.
# 문자를 정수형으로 형변환해서 각 변수에 담는다.

# 총점을 계산한다.
# 평균을 계산한다.

# 평균점수가 90점 이상이면 A
# 평균점수가 80점 이상이면 B
# 평균점수가 70점 이상이면 C
# 평균점수가 60점 이상이면 D
# 평균점수 그 외 F

kor, eng, mat = input("국어, 영어, 수학 점수를 입력하세요.  :").split()

kor, eng, mat = int(kor), int(eng), int(mat)

tot = kor + eng + mat
avg = tot / 3

print(kor, eng, mat, tot, avg)

if avg >= 90:
    print("평균점수: ", avg, "A학점 입니다.")
elif avg >= 80:
    print("평균점수: ", avg, "B학점 입니다.")
elif avg >= 70:
    print("평균점수: ", avg, "C학점 입니다.")
elif avg >= 60:
    print("평균점수: ", avg, "D학점 입니다.")
else :
    print("평균점수: ", avg, "F학점 입니다.")
    