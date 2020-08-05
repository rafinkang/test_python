# 클라이언트 사이드
from socket import *

ip = "127.0.0.1"
ip = "192.168.0.2"
port = 5000


clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip, port))

while True:
    sendData = input(">>>")
    clientSock.send(sendData.encode("utf-8"))

    recvData = clientSock.recv(1024)
    print("서버가 보낸메세지 :", recvData.decode("utf-8"))