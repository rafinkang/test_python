# 매직함수 : __가장일반적인 용도__ : 오퍼레이터 오버로딩용으로 가장 많이 쓴다.
# +  : __add__
# -  : __sub__
# *  : __mul__
# /  : __truediv__
# // : __floordiv__
# %  : __mod__
# ** : __pow__  
# <  : __lt__   less then
# >  : __gt__   grate then
# >= : __ge__   grate equal
# __del__ = 소멸자
# __str__ = str() 함수에 넣으면 실행

class Car:
    # 생성자
    def __init__(self):
        print("---초기화 함수---")

    # 소멸자
    def __del__(self):
        print("소멸자 호출: 메모리에서 더 이상 이 객체를 사용하지 않는다")


    def __str__(self):
        # 문자열화 해서 반환
        return "str method가 호출됨"

c2 = Car()
print(str(c2))  #str method가 호출됨

del c2  #c2 객체를 메모리에서 제거 