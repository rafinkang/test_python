# 서버에서 
import socket
import threading

# 접속 정보 
host = ""
port = 5000

# 서버 시작 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# 여러 사용자의 접속 허용 
clients = [] 
nicknames = [] 

# 접속 중인 모든 사용자에게 메세지 전달
def broadcast(msg):
    for client  in  clients:
        client.send(msg)

# 클라이언트의 메세지 처리하는 함수 
def handle(client):
    while True:
        try:
            # 클라이언트 메세지 수신 
            msg = client.recv(1024)
            # 브로드캐스트 
            broadcast(msg)
            # 화면에 출력 
            print(msg.decode("utf-8"))
        except:
            # 제거 하고 클라이언트 닫기 
            index = clients.index(client)
            # 예외 발생한 클라이언트만 리스트에서 제거 
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} 떠남!! ".format(nickname).encode("utf-8"))
            nicknames.remove(nickname)
            break


# 리스닝 함수 
def receive():
    while True:
        print("클라이언트 연결 대기중")
        connectionSock, addr = server.accept()
        print(str(addr) + "로부터 연결됨")

        # 별명을 요청하고 저장 
        connectionSock.send("NICK".encode("utf-8"))
        nickname = connectionSock.recv(1024).decode("utf-8")
        print(nickname)
        # 별명 리스트에 별명담기 
        nicknames.append(nickname)
        # 접속 소켓 리스트에 현재 소켓을 담기 
        clients.append(connectionSock)

        #접속자 소개해주기 
        broadcast("{} 님이 접속하셨습니다. ".format(nickname).encode("utf-8"))
        connectionSock.send("서버에 접속되었습니다. 환영합니다.".encode("utf-8"))

        #핸들링 함수를 쓰레드 
        t = threading.Thread(target=handle, args=(connectionSock,))
        t.start()

receive()



