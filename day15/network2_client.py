# 클라이언트 사이드
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
# 서버로 연결해줘
# 127.0.0.1 - 루프백 어드레스 
# clientSock.connect(('127.0.0.1', 5000))
clientSock.connect(('192.168.0.2', 5000))
# clientSock.connect(('192.168.0.69', 5000))
# clientSock.connect(('192.168.0.68', 5000))
clientSock.send("Hello~~~~~~~~kkk go home plz".encode("utf-8"))

data = clientSock.recv(1024)
print("서버가 보낸 데이터:", data.decode("utf-8"))

print("연결 성공!!")

