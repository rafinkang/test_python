'''
is - a 관계 -> 상속
둘 사이가 밀집

Aggregation Relationship    : 경찰 <==> 총 의 관계
has - a 관계
둘 사이가 유연한? 느슨한 관계

Composition Relationship    : 자동차 <==> 엔진 의 관계
'''
class Engine:
    def __init__(self):
        print("새로운 엔진입니다.")
    
    def start(self):
        print("엔진 동작하는중")

class Car:
    def __init__(self):
        print("붕붕카~~")
        self.engine = Engine()
        print("엔진 장착 !")
    
    def run(self):
        self.engine.start()

c = Car()
c.run()
