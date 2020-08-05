# 서버 사이드
from socket import *

port = 5000

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(3)
print("%d번 포트로 접속 대기중.."%port)


connectionSock, addr = serverSock.accept()

print(str(addr), "에서 접속되었습니다.")

while True:
    recvData = connectionSock.recv(1024)
    print("클라이언트가 보낸 메세지 :", recvData.decode("utf-8"))

    sendData = input(">>>")
    serverSock.send(sendData.encode("utf-8"))