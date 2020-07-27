# 15. 비의 깡 가사를 rain.txt 파일에 저장하세요 
ggang = """
Yeah 다시 돌아왔지
내 이름 레인(RAIN)
스웩을 뽐내 WHOO!
They call it! 왕의 귀환
후배들 바빠지는 중!
신발끈 꽉 매고
스케줄 All Day
내 매니저 전화기는
조용할 일이 없네 WHOO!

15년을 뛰어
모두가 인정해 내 몸의 가치
허나, 자만하지 않지
매 순간 열심히 첫 무대와 같이
타고난 이 멋이 어디가
30 sexy 오빠
또 한번 무대를 적셔
레인이펙트
나 비 효과

화려한 조명이 나를 감싸네
시간이 멈추길 기도해
but, I’m not gonna cry yeah
불 꺼진 무대 위 홀로 남아서
떠나간 그대의 목소릴 떠올리네
나 쓰러질 때까지 널 위해 춤을 줘

허세와는 거리가 멀어
난 꽤 많은 걸 가졌지
수많은 영화제 관계자
날 못 잡아 안달이 나셨지
귀찮아 죽겠네 알다시피
이 몸이 꽤 많이 바빠
섭외 받아 전세계 왔다 갔다
팬들이 하늘을 날아 WHOO!

TV 드라마, 영화 yeah!
I get it all
이젠 모두를 붙잡을 노래를 불러
볼륨은 올리고
재 등장과 동시
완전 물 만나 call me 나쁜 오빠
무대를 다시 한번 적시지
레인이펙트
나 비 효과

화려한 조명이 나를 감싸네
시간이 멈추길 기도해
but, I’m not gonna cry yeah
불 꺼진 무대 위 홀로 남아서
떠나간 그대의 목소릴 떠올리네
나 쓰러질 때까지 널 위해 춤을 줘
"""

with open("./day9/rain.txt", "w", encoding="utf-8") as file:
    file.write(ggang)

# 16.
# 	rain.txt 에서 4글자 단어는 모두 몇개인가? 
import re
with open("./day9/rain.txt", "r", encoding="utf-8") as file:
    cnt = 0
    for word in file.read().split():
        if len(re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', word)) == 4:
            # print(word)
            cnt += 1
    print(cnt)

# 17.
# 사용자가 입력한 디렉토리의 파일과 디릭토리 목록을 dir.txt 파일에 저장하세요
# 입력: c:/

import os

user_dir = input("디렉토리를 입력하세요. :")
dir_list = os.listdir(user_dir)

with open("./day9/dir.txt", "w", encoding="utf-8") as file:
    for dirs in dir_list:
        file.writelines(dirs+"\n")


# 18.
# 	로또 번호를 생성해서  lotto.txt 파일에 한줄씩 저장하세요 
# ex)
# 	3
# 	15
# 	29
# 	32
# 	35
# 	41

import random

lotto = []
for i in range(6):
    lotto.append(random.randint(1, 45))

with open("./day9/lotto.txt", "w", encoding="utf-8") as file:
    for num in lotto:
        file.writelines(str(num)+"\n")

# 19.
# 	랜덤하게 소문자 3자를 생성해서  randomchar.txt 파일에 저장하세요 
# 소문자 askii 97~122

char = ''
for i in range(3):
    char += chr(random.randint(97,122))

with open("./day9/randomchar.txt", "w", encoding="utf-8") as file:
    file.write(char)


# 20.  다음 내용을 stock.csv 로 저장하세요 

# 	종목번호  회사명   현재주가 
# 	035720  카카오   326500
#  	005930  삼성전자  55600
# 	047820  초록뱀     1590 

# 종목번호,회사명,현재주가 
# 035729,카카오,326500

with open("./day9/stock.csv", "w", encoding="utf-8") as file:
    file.writelines('종목번호,회사명,현재주가\n')
    file.writelines('035729,카카오,326500\n')
    file.writelines('005930,삼성전자,55600\n')
    file.writelines('047820,초록뱀,1590\n')