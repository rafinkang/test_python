# csv 파일 
# a, b, c = input("숫자 3개를 콤마로 구분해서 입력하세요 : ").split(',')

# print("a :", a, "b :", b, "c :", c)

print(100,200,300,sep=", ")

print("Hello", "python", "world", sep=" ")

print(100, 200, 300, sep="\n")
# 특수문자 
# 엔터 : \n - 개행문자 캐리지 리턴 아랫줄로
# 탭 ; \t 

print("아\t날씨가 좋다\n집에가야지\n룰루룰루루루루룰루~~")

print("오늘은", end="\t") # 오늘은 \n 이 자동으로 들어가있다.
print("수요일", end=", ") # end="" \n대신 다른 문자열로 대체
print("내일은", end="\t")
print("목요일", end="\t")
print("주말은 언제오나")


# year, month,day,hour,minute,second 변수를 선언하고
# 값을 대입한 후에
# 아래와 같은 출력을 얻도록 코드를 작성해 보세요.
# 오늘은 2020/7/15 18:00:00 입니다.

year, month, day, hour, minute, second = '2020', '7', '15', '18', '00', '00'

print('오늘은 ' + year, month, day, sep="/", end=" ")
print(hour, minute, second, sep=":", end=" 입니다.")


# 사용자가 입력한 3개의 숫자중 가장 큰 수를 출력
