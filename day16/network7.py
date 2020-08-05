# 서버 사이드
from socket import *
import threading
import time

port = 5000

def send(sock):
    sendData = input(">>>")
    sock.send(sendData.encode("utf-8"))

def receive(sock):
    recvData = sock.recv(1024)
    print("클라이언트 메세지 :", recvData.decode("utf-8"))

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print("%d번 포트로 접속 대기중.."%port)
connectionSock, addr = serverSock.accept()
print(str(addr), "에서 접속되었습니다.")

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(0.5)
    pass