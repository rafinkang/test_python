# 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈 : os
import os
# print(dir(os))

# 현재 작업 디렉토리
print(os.getcwd(), os.getcwdb())

# 현재 작업디렉토리에 있는 파일과 디렉토리 목록 검색
print(os.listdir())
print(os.listdir('day9'))   
print(os.listdir('.'))      # .  현재 디렉토리 : E:\dev\python_workspace
                            # .. 부모 디렉토리 : E:\dev
print(os.listdir('E:\dev\python_workspace'))
print('---------------------------------------------------------')
# 현재 작업디렉토리에 있는 모든 파일을 출력
# 반복문을 사용해서 한개씩 출력
# 확장자가 .zip인 파일들만 선택
# for file in os.listdir("e:/"):
#     if file.split('.')[-1] == 'zip':
#         print(file)

for file in os.listdir("e:/"):
    if file.endswith("zip"):    #endswith 확장자검색
        print(file)

