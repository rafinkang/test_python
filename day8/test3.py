def sayHello():
    msg = "니하오"
    def prt():      #중첩함수 
        print(msg)
    prt()

sayHello()
        
print('------------------------------------')

def f1():
    a = 10      #f1의 지역변수
    def f2():   #f1안에있는 중복함수 f2
        # global a
        nonlocal a #바로 위 영역의 a를 지칭  
        a = 20  #f2의 지역변수
    f2()
    print(a)
f1()