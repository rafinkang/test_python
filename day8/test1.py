keyword = "오늘은 비가 언제 까지 올까요?".split()

print(keyword, type(keyword))

# 각 단어가 몇글자인지 알아 내기

print({len(word) for word in keyword} , type({len(word) for word in keyword}))

# 3자 초과된 단어만 선택해서

print({len(word) for word in keyword if len(word) > 3 })

# dictionary(JSON) Comprehesion

countrys = {"한국":"서울", "일본":"도쿄", "중국":"북경", "UAE":"아부다비"}

# 키값만 출력

capital = {country : capital for country, capital in countrys.items()}
print(capital)