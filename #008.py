class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.\n".format(self.name))
    
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드: 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐: 지상 유닛, 기동성이 좋음.
vulture = AttackUnit("벌쳐", 80, 10, 20)
# 배틀크루저: 공중 유닛, 체력과 공격력 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시") # name, lcation 제공해줘야 함.
battlecruiser.move("9시") # self.name이므로 location만 제공해줘도 됨.

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass # 일단 넘어가겠다. 실행되나 pass 지점에서 종료처리.
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # self 없이 사용한다.
        self.location = location

# 서플라이 디폿: 건물, 1 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass

'''
class Unit:
    def __init__(self):
        print("Unit 생성자")
    
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__() # 처음 부모 클래스만 호출된다.
        Unit.__init__(self)
        Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit()
'''
