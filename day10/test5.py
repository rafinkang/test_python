'''
    OOP : Object Oriented Programming - 객체 지향 프로그래밍
        : 목적 -> 자원의 재활용
    클래스를 사용해 객체(instance)를 생성
    클래스는 새로운 이름 공간을 지원하는 단위

    isinstance(변수, 클래스명) - 어느 클래스를 사용했는지 알아보는 함수
    isinstance(obj, class_or_tuple) -> bool
        Return whether an object is an instance of a class or of a subclass thereof.
        A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.


'''
class Car:    
    def __init__(self, name, color, birth):
        # 차명
        self.name = name    # 인스턴스 변수
        # 색상
        self.color = color
        # 연식
        self.birth = birth
        # 바퀴
        self.wheel = 4
        # 핸들
        self.handle = 1

    # 전진()
    def go(self):       # 인스턴스 함수
        print('전진')
    # 후진()
    def back(self):
        print('후진')
    # 깜빡이()
    def ggambbak(self):
        print('깜빡깜빡')
    # 가속()
    def acel(self):
        print('가속')
    # 감속()
    def breaking(self):
        print('감속')
    # 정지()
    def stop(self):
        print('정지')

    def status(self):
        print('차명:',self.name)
        print('색상:',self.color)
        print('연식:',self.birth)
        print('바퀴:',self.wheel)
        print('핸들:',self.handle)
        
c1 = Car('차아', '흰둥이', 2020)
c1.status()

# 파이썬 메서드의 첫번째 파라미터 명은 관례적으로 self 이름 사용
# 호출 시 객체 자신이 전달 되기 때문에 self 이름 사용
c1.go()
Car.go(c1)

print(isinstance(c1, Car))
