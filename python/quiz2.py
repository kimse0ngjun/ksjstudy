# 오프라인 스터디 모임 날짜 정하기
# 조건 1: 랜덤으로 날짜 뽑기
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
from random import *

day = randint(4, 28)

print("오프라인 스터디 모임 날짜는 매월", day, "일로 선정되었습니다.")