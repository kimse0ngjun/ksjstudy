class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 순서상, 마지막에 상속받는 클래스만 호출함
        Unit.__init__(self)
        Flyable.__init__(self)
        
# 드랍쉽
dropship = FlyableUnit()