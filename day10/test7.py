import log as log
class ATM:
    def __init__(self):
        print('----------초기화 함수----------')
        self.name = "홍길동"
        self.balance = log.readBalance("./day10/bank.log")

    def deposit(self, money):
        self.balance += money
        log.saveLog("./day10/bank.log", money, self.balance, False)
        print("%s 원 입금이 완료되었습니다. \n 현재 잔액은 %s 원 입니다."%(format(money,','), format(self.balance, ',')))
    
    def withDraw(self, money):
        # db에 연결해서 현재 진짜 잔액이 존재하는지
        # 권한으 ㄴ있는지
        # 감사기록을 남긴다(로그)

        # 작업디렉토리에 bank.log 파일을 생성
        # 지금시간, 출금액, 현재잔액을 남긴다
        
        if self.balance - money > 0:
            self.balance -= money
            log.saveLog("./day10/bank.log", money, self.balance, True)
            print("%s 원 출금이 완료되었습니다."%(format(money,',')))
        else:
            print('잔액이 부족합니다.')

        print('현재 잔액은 %s원 입니다.'%(format(self.balance, ',')))

    



auto = ATM()

# print(auto)
# auto.deposit(100)
auto.withDraw(1000000)