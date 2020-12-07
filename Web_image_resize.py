'''
다운로드 받은 이미지들을 resize_파일명
100,100으로 변경

다운로드받은 이미지 폴더명
폴더내에 있는 모든 파일의 목록 구하기
파일 확장자가 png, gif, jpg 인 파일만 선택
이미지 객체로 변환
100, 100으로 resize
resize_파일명 형식으로 저장
'''

from PIL import Image
import os

file_list = os.listdir('./아이유')
# print(file_list)

for f in file_list:
    if f.split('.')[-1] in ['jpg','png','jpeg','gif']:
        img = Image.open('./아이유/' + f)
        img = img.resize((100,100))
        img.save('./iu_100x100/resize_'+f)
        
    