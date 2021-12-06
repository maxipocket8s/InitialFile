# 클래스

# 마린: 공격 유닛, 군인. 총을 쓸 수 있음.
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 탱크. 포를 쓸 수 있는데 일반 모드와 시즈 모드가 있음.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(hp, damage))
    
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# 멤버 변수 # 클래스 내 변수 ex. name, hp, damage

# 레이스: 공중 유닛, 비행기. 클로킹(적군에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage)) # 클래스 외부에서 멤버 변수를 쓸 수 있다.

# 마인드 컨트롤: 적군 유닛을 내 것으로 만듦
wraith2 = Unit("뺏은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 객체에 변수를 추가할 수 있음
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name)) # Error

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 15)
firebat1.attack("5시")
firebat1.damaged(25) # 1차 공격 받음.
firebat1.damaged(25) # 2차 공격 받음.


# 상속
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.init_hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
class AUnit(Unit):
    def __init__(self, name, hp, damage, life):
        Unit.__init__(self, name, hp, damage)
        self.life = life
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0 and self.life >= 1:
            self.life -= 1
            self.hp = self.init_hp
            print("{0}: 파괴되어 다시 생성되었습니다. [잔여 목숨 {1} / 체력 {2}]\n".format(self.name, self.life, self.hp))
        elif self.hp <=0 and self.life == 0:
            print("{0}: 파괴되었습니다.\n".format(self.name))
firebat2 = AUnit("파이어뱃", 50, 15, 2)
firebat2.attack("2시")
firebat2.damaged(25)
firebat2.damaged(25)
firebat3 = AUnit("파이어뱃", 45, 15, 2)
firebat3.attack("2시")
firebat3.damaged(25)
firebat3.damaged(25)
firebat3.damaged(25)
firebat3.damaged(25)
firebat3.damaged(25)
firebat3.damaged(25)