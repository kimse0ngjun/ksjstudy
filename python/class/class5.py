# 다중 상속
# 메소드 오버라이딩 - 객체 지향 프로그래밍에서 부모 클래스에서 정의된 메서드를 자식 클래스에서 재정의
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp, 0)  # speed 기본값 0 설정
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
            
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)  # 수정된 부분
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # 부모 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 20)
vulture.move("11시")

# 배틀크루저
battles = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battles.move("9시")


# pass

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 넘어감(완성된 것처럼 보이도록 함함)

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") 

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    pass

game_start()
game_over()


# super
class BuildingUnit2(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(self, name, hp, 0)
        self.location = location
