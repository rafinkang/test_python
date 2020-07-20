msg = "HELLO"
print(msg)

# 이 글자를 소문자로 변환 시키고자 합니다.
print(msg.lower())
# 1. 각 글자의 ASCII코드 값을 구한다.
print(len(msg))
for i in range(len(msg)):
    # print(msg[i], ord(msg[i]))
    code = ord(msg[i]) #이 글자의 ascii code
# 2. 대문자의 범위 : 65~90 이라면 이것을 대문자로 바꾼다.
#    소문자   : 97~122   -> 대문자 코드 +32
    if code >= 65 and code <= 90:
# 3. 변환된 값을 코드로 출력
        print(chr(code+32), end ="")
# hello


