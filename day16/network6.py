# 클라이언트 사이드
from socket import *

ip = "127.0.0.1"
ip = "192.168.0.2"
port = 5000

def send(sock):
    sendData = input(">>>")
    sock.send(sendData.encode("utf-8"))

def receive(sock):
    recvData = sock.recv(1024)
    print("서버가 보낸메세지 :", recvData.decode("utf-8"))



clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip, port))

while True:
    send(clientSock)
    receive(clientSock)