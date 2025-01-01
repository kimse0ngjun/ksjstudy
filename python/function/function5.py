gun = 10

def checkpoint(soldiers): # 경계근무
    # gun = 20 # 지역변수
    global gun # 전역 공간에 있는 gun 사용(전역변수 사용(global))
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 님은 총 : {0}".format(gun))
    return gun # 바뀐 gun 변수를 외부로 보냄
    
    
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

