a = 10          # 전역 변수
def prt():
    global a    # 전역변수 쓸거임
    a = 20      # 지역 변수
    print(a)
    print(locals()) #지역변수 목록 호출 함수
    # print(b)

prt()
print('-------------전역변수 영역------------------')
print(locals())
print(a)