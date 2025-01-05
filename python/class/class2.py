# 클래스: 객체를 생성하기 위한 탬플릿릿
# 클래스 사용 - 코드 재사용성을 높히고, 데이터를 구조화하여 프로그램을 더 체계적으로 설계하는 데 도움을 준다.
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수 - 클래스 내에서 선언된 변수
        self.hp = hp
        self.damage = damage 
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__: 객체가 생성될 때 자동으로 호출되는 초기화 메서드
# marine3 = Unit("마린", 3) -> self를 제외한 모든 객체 수를 선언해야지 Unit 클래스를 사용할 수 있음음

# 레이스
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤
# 멤버변수는 클래스 내부에서 확장할 수 있고, 멤버변수로 확장된 객체 내에서만 적용됨(wraith1에서는 clocking이 적용안됨됨)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
    
    