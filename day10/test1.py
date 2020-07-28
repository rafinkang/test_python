'''
class 클래스명:
    # Object 설계 - 객체 모델링
    Object      - 사람
    속성        - 눈 코 입 귀 이름
    method      - 생각() 먹기() 말하기() 걷기()


    함수,method()
    객체 : 사물
    class : 설계도
    대상 : instance

'''

class Human:
    # __매서드__ : 매직메서드
    def __init__(self):
        print("초기화 함수")

    def eating(self):
        print("냠냠 처묵")

    def sleeping(self):
        print("쿨쿨zZzZ")

    
    



hong = Human()  # instance - Human class를 사용해서 hong이라는 하나의 객체를 만듦 
                # hong = new Human();
print(hong)     # <__main__.Human object at 0x016D1F88>

a = 10
print(type(a))  # <class 'int'>

hong.eating()
hong.sleeping()

print('---------------------------------------')

lucy = Human()

lucy.eating()
lucy.sleeping()

