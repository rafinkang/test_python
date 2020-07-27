# 현재 작업중인 디렉토리 경로를 얻어오기
import os
dir = os.getcwd()
print(dir)

# 파일 입출력
# 파일 열기 os.open("파일명","모드") ex) <_io.TextIOWrapper name='./day9/hello.txt' mode='r' encoding='cp949'>
file = open('./day9/hello.txt', "r")
print(file)
# 파일 읽기 file.read() ex) <class 'str'>
print(file.read(), type(file.read()))
# 파일 닫기
file.close()

print('-------------------------------------------')
file2 = open("./day9/hello2.txt", "w")
print(file2)
file2.write("금요일 같은 월요일..월요병 ㅠㅠ ")
file2.close()