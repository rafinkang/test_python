import time
def saveLog(savedir, money, balance, mode):
    if mode:
        type = "출금"
    else:
        type = "입금"
    input_text = time.ctime()+", "+type+", "+str(money)+", "+str(balance)+"\n"

    with open(savedir, "a", encoding="utf-8") as file:
        file.write(input_text)

def readBalance(savedir):
    with open(savedir, "r", encoding="utf-8") as file:
        return int(file.readlines()[-1].split(',')[-1])