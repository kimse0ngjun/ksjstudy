# 모듈 - 파일과 같은 경로이거나 파이썬 라이브러리에 있는 파일들만 사용 가능능

# 일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))
    
# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다".format(people, people * 6000))

# 군인할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))