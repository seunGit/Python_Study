class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        # 다중상속 받을 시 super()를 사용하면 먼저 상속받는 클래스만 호출됨.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 생성
dropship = FlyableUnit()