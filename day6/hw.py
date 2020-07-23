# 1. 
# 세계 최초의 암호화   : setEncryption(문자열) 

# 	1. 사용자로부터 단어를 입력받는다.    ex) HELLO 
		  
# 	2. 3번째 뒤에 글자를 출력한다.         ex) ~~~~~ 

# 	예) A ==> D
# 	    C ==> F
# 	    B ==> E 

# 	getDecode(~~~~~)
# 	HELLO 

# ord() <> chr()
# 4. 대문자 : 65~90    소문자 :97~122
def setEncryption(word) :
    result = ''
    for i in word:
        ascii_code = ord(i)
        ascii_code += 3
        if (ascii_code > 90 and ascii_code < 97) or ascii_code > 122:
            ascii_code - 25
        result += chr(ascii_code)
    return result

def getDecode(word) :
    result = ''
    for i in word:
        ascii_code = ord(i)
        ascii_code -= 3
        if ascii_code < 65 or (ascii_code < 97 and ascii_code > 90):
            ascii_code + 25
        result += chr(ascii_code)
    return result

w = input("인코딩 할 단어를 입력하세요. : ")
set_word = setEncryption(w)
print(set_word)
print('-------------------------------------')

w2 = input("디코딩 할 단어를 입력하세요. : ")
get_word = getDecode(w2)
print(get_word)

print('-------------------------------------')
# 2.

# score 리스트에 국어 , 영어 , 수학 점수가 들어있다.
# 총점과 평균을 계산해서 리스트에 담은 후 모든
# 학생의 국어, 영어, 수학, 총점, 평균을 출력하시오
# 참고) 리스트에는 국어, 영어 수학 점수만 들어있다.

score = [
	[80,80,80,0,0],
	[60,50,80,0,0],
	[50,90,90,0,0],
	[40,50,60,0,0],
	[90,90,95,0,0],
	[85,95,100,0,0] ]

for i in score:
    tot = i[0] + i[1] + i[2]
    avg = tot / 3
    i[3] = tot
    i[4] = avg

print(score)
print('-------------------------------------')

# 3.

# 야구 게임 (BaseBall)
# 3자리의 숫자 랜덤 생성 : 397
# 자리와 숫자가 모두 동일 하면 strike
# 자리는 다르지만 다른 자리에 숫자가 존재하면 볼

# 입력:307
# 출력 : 2S

# 입력:379
# 출력: 1S2B

# 입력:397
# 출력: 정답 축하합니다. 3회만에 성공하셨습니다.

# [알고리즘]
# 1. 컴퓨터가 세자리숫자를 생성한다.
# 2. 사용자로부터 3자리숫자를 입력받는다.
# 3. 판별한다.
# 	(자리와 숫자가 일치하면 :strke
# 	자리는다르지만 숫자가일치하면 : ball)
# 4. 출력한다.
# 5. 3strike이면 종료한다.
# 6. 아니면 2번으로 돌아가서 반복한다.
print("야구게임 시작 !")
print('-------------------------------------')

import random

bingo_list = []
while len(bingo_list) < 3:
    temp = str(random.randint(1, 9))
    if temp in bingo_list:
        continue
    else:
        bingo_list.append(temp)

# print(bingo_list)
cnt = 0
while True:
    user_input = list(input("3자리 숫자를 입력하세요. : "))
    strike = 0
    ball = 0
    cnt += 1
    for i in range(3):
        if user_input[i] == bingo_list[i]:
            strike += 1
        elif user_input[i] in bingo_list:
            ball += 1
        
    if strike == 3:
        print("축하합니다. "+str(cnt)+"회 만에 성공하셨습니다.")
        break
    else:
        print(strike,"S",ball,"B !!")



# 1002235976311