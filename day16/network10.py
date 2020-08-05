# 클라이언트 사이드
import socket
import threading

ip = "192.168.0.68"
port = 5000

# 닉네임 결정
nickname = input("당신의 닉네임을 입력하세요 : ")

# 서버에 연결
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((ip, port))

# 서버에 닉네임을 보내기
def receive():
    while True:
        try:
            msg = clientSock.recv(1024).decode("utf-8")
            if msg == "NICK":
                clientSock.send(nickname.encode("utf-8"))
            else:
                print(msg)
        except:
            # 에러발생시 연렬끊기
            print("에러발생@)@)@)(@(@(@")
            clientSock.close()
            break

# 서버에 메세지 보내기
def send():
    while True:
        msg = "{}: {}".format(nickname, input(''))
        clientSock.send(msg.encode("utf-8"))

# 수신과 발신을 동시에 처리하기 위해 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()
        
