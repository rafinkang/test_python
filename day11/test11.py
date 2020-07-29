from test10 import Parent

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.score = 100
        self.name = "홍길동"
        self.age = 20

    def goClub(self):
        print("움칫 둠칫~")
    
    # method overriding
    def singing(self):
        print("와 여름이다~~")

if __name__ == "__main__":
    c = Child()
    print(c.score)
    print(c.name)
    print(c.age)

    c.eating()
    c.singing()
    c.goClub()