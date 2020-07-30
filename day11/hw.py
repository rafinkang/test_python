# 1.   object , class , instance 란? 
'''
Class
Obejct를 만들어 내기 위한 설계도 혹은 틀, 연관되어 있는 Variable와 Method의 집합

Object
소프트웨어 세계에 구현할 대상, Class에 선언 된 모양 그대로 생성된 실체
Class의 타입으로 선언되었을 때 'Object'라고 부른다
ex) m = Man() -> m은 Man클래스를 선언한 오브젝트

Instance
설계도를 바탕으로 소프트웨어 세계에 구현된 구체적인 실체
즉, 객체(Object)를 소프트웨어에 실체화 하면 그것을 'Instance'라고 부른다.
실체화된 Instance는 메모리에 할당된다.

'''
# 2.    
class Man():
    def __init__(self):
        self.name = "홍길동"
        self.eye = 2
        self.gender = "남"
        self.arm = 2
        self.age = 20
        self.job = "도적"
        self.character = "스틸"
    
    def steal(self):
        print("내꼬내꼬 다 내꼬얌!!!")
    def run(self):
        print("헛둘 헛둘")
    def runrun(self):
        print("땀나게 달려요")
    def magic_move(self):
        print("동해 번쩍 서해 번쩍")
	
m = Man()

print(m.name) # 홍길동
print(m.eye) # 2 
print(m.gender)# 남
print(m.arm) # 2
print(m.age) # 20
print(m.job) # 도적
print(m.character)# 스틸 

m.steal() # 내꼬내꼬 다 내꼬얌!!! 
m.run() # "헛둘 헛둘"
m.runrun() # "땀나게 달려요
m.magic_move() # 동해 번쩍 서해 번쩍


# 3.	변수명명법?
'''
Google 스타일 가이드 ------------
글로벌--
GLOBAL_CONSTANT_NAME

--  CamelCase   --
ClassName
ExceptionName

--  mixCase     --
????

--  snake_case  --
module_name
package_name
method_name
function_name
global_var_name
instance_var_name
function_parameter_name
local_var_name

--------------------------------
'''
# 4. 
# 	ex4.py 
# ----------------------------------------
# 	class Triangle 
# 	width , height
# 	getArea()
# ----------------------------------------	
# 	triangle =	Triangle (100,200) # 너비 100, 높이 200 
# 	print(triangle.getArea())  # 삼각형의 너비 구하기 

# print('------------------------------------')
# class Triangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def getArea(self):
#         return self.width * self.height / 2

# triangle =	Triangle (100,200)
# print(triangle.getArea())
# 5. 
# 	ex5.py
# ----------------------------------------
# 	class Rectangle
# 	width , height
# 	getArea()
# ----------------------------------------
# 	r = Rectangle(200,300)
# 	print(r.getArea())  # 사각형의 너비 구하기 

# print('------------------------------------')
# class Rectangle():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def getArea(self):
#         return self.width * self.height

# r = Rectangle(200,300)
# print(triangle.getArea())

# 6.
# 	ex6.py
# 	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
# 	작성하세요 
print('------------------------------------')
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height        
	
# 7. 
# 	Rectangle, Triangle 은 Figure 클래스의 구현클래스로 코드를 변경합니다.
# 8. 
# 	Rectangle, Triangle 의 getArea() 는 Figure 클래스 의 getArea() 를 
# 	method overriding 시켜줍니다. 
print('------------------------------------')
class Triangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)
        # self.width = width
        # self.height = height

    def getArea(self):
        return self.width * self.height / 2

triangle =	Triangle (100,200)
print(triangle.getArea())
print('------------------------------------')
class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(width,height)
        # self.width = width
        # self.height = height
    
    def getArea(self):
        return self.width * self.height

r = Rectangle(200,300)
print(r.getArea())
# 9.
# 	두점 사이의 거리를 계산하는 pythagoras()를 완성하세요 

# 	print(util.pytagoras(100,100, 200 ,200))
	
# 	참고 : math.sqrt(4) ==> 2 
import math
class Util:
    def __init__(self):
        # self.xx = 0
        # self.xy = 0
        # self.yx = 0
        # self.yy = 0
        pass
    
    def pytagoras(self, xx, xy, yx, yy):
        x = xx - yx
        y = xy - yy
        return math.sqrt(x**2 + y**2)

util = Util()
print(util.pytagoras(100,100,200,200))

# 10.	아래의 명령이 수행될수 있는 Point 클래스를 작성하세요 

# 	p = Point(100,100) # (x, y) 좌표 
# 	p.set_x(200)  # x좌표값을 200으로 변경
# 	p.set_y(300)  # y좌표값을 300으로 변경

# 	p.get_xy() # (200,300) 형태로 출력 
	
# 	p.move(500,300) # (200,300) ==> (500,300)
# 	                     # 메세지를 출력하고 x <= 500 y <=300을 담는다.
	
# 	참고 ) 모든 메세드는 인스턴스 메서드 모든 속성는 인스턴스 속성

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, num):
        self.__x = num

    def set_y(self, num):
        self.__y = num
    
    def get_xy(self):
        print("(",self.__x,",",self.__y,")")
    
    def move(self, x, y):
        print("(",self.__x,",",self.__y,") ==> (", x, ",", y,")")
        self.__x = x
        self.__y = y

p = Point(100,100) # (x, y) 좌표 
p.set_x(200)  # x좌표값을 200으로 변경
p.set_y(300)  # y좌표값을 300으로 변경

p.get_xy() # (200,300) 형태로 출력 
p.move(500,300) # (200,300) ==> (500,300)
                        # 메세지를 출력하고 x <= 500 y <=300을 담는다.