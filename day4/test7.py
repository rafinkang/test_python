# 
# 쥐띠

# 태어난 연도를 입력하면 어떤 띠인지를 출력

# 태어난 년도를 4자리로 입력: 2020
# 당신은 쥐띠 입니다.

year = int(input("태어난 년도를 4자리로 입력: "))

# 자 축 인 묘 진 사 오 미 신 유 술 해
# 쥐 소 호랑이 토끼 용 뱀 말 양 원숭이 닭 개 돼지
# 쥐띠 = 4

ddi = ['쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지' ]
print(year,"년 은", ddi[year%12 - 4], "띠 입니다.")

# -----------------------------------------------------

zodiac = ["양띠", "원숭이띠", "개띠", "돼지띠", "쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠", "말띠"]
year = int(input("태어난 년도를 4자리로 입력: "))
year %= 12
print("당신의 띠는", zodiac[year], "입니다.")
