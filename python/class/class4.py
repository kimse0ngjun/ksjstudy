# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name # 멤버변수 - 클래스 내에서 선언된 변수
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 상속(멤버변수가 같을 경우 "클래스 변수()" 형태로 사용됨)
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 클래스 변수.__init__(self, 멤버변수, ..) 형태로 사용
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕(공격력 없음)
            
# 파이어뱃    
fire1 = AttackUnit("파이어뱃", 50, 16)
fire1.attack("5시")
# 공격 2번 받는다고 가정
fire1.damaged(25)
fire1.damaged(25)