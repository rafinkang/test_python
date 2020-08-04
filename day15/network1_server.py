from socket import *
import random

# ipV4 - TCP/IP 방식으로 선언
serverSock = socket(AF_INET, SOCK_STREAM)

# 65535 ==> 8000 ~ 9000 포트 만 개발용으로 열어놓음
serverSock.bind(('',5000))    # 5000번 포트 사용
print("사용자의 접속을 대기합니다.")
serverSock.listen(1)    # 연결을 기다림 (수신중..)
connectionSock, addr = serverSock.accept()
print(str(addr)+"연결 성공 !!!")

data = connectionSock.recv(1024)
msg = data.decode("utf-8")
print(msg)
msglist = [
    "응",
    "아니",
    "집에 가",
    "ㅇㅋㅇㅋ",
    "꾸이이익",
    "배고파ㅏ퉤퉤",
    "집갈래ㅐㅐ",
    "보내줘ㅓㅓㅓ",
    "재밌는거 하자",
    "으어어어어어ㅓㅓ"
]

# 반사~
# connectionSock.send(msg.encode("utf-8"))
connectionSock.send(msglist[random.randint(0,len(msglist)-1)].encode("utf-8"))
print("서버 메세지 전송 완료")