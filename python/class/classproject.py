from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit): 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # speed 기본값 0 설정
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
            
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 5)  # 인자 수 수정
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False  # 시즈모드 개발 여부
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 2, 35)  # 인자 수 수정
        self.seize_mode = False
    
    def set_seize_mode(self):
        if not Tank.seize_developed:
            return
        
        # 시즈모드 아닐 때 -> 시즈모드
        if not self.seize_mode:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage //= 2  # 정수 나눗셈으로 변경
            self.seize_mode = False
            
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, speed)  # 수정된 부분
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # 부모 클래스의 move() 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 7, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)
    
    def clocking(self):
        if self.clocked:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))  # 오타 수정
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
            

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 게임 시작    
game_start()

# 마린 3기
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 1기
t1 = Tank()
t2 = Tank()

# 레이스 1기
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발    
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # 지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
# 전군 공격        
for unit in attack_units:
    unit.attack("1시")
    
# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5 ~ 20)
    
# 게임 종료
game_over()
    
    