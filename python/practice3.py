# 섹션 3 ~ing
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 1
print(number)

## 숫자 처리함수

# abs(절댓값)
print(abs(-5)) # absolute = 5

# pow(제곱형태 표현)
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 최대값 찾아주기 12
print(min(5, 12)) # 최소값 찾아주기 5

# round(반올림)
print(round(3.14)) # 3 
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4