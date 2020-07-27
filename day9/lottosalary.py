import random
def raise_rnd_salary(sal):
    rnd = random.randint(0,1)
    if rnd%2 :
        print("강화성공 !!")
        sal *= 1.2
    return int(sal)
def reduce_rnd_salary(sal):
    rnd = random.randint(0,1)
    if rnd%2 :
        sal *= 0.8
    return int(sal)

if __name__ == "__main__":
    raise_rnd_salary(2000)
    reduce_rnd_salary(2000)



    