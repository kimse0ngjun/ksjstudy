# 섹션 3 연산자
print(1+1) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1 
print(5//3) # 몫 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True


# 비교 연산자
print(1 != 3) # True (1은 3이 아니다. 같은 값이 아님)
print(not(1 != 3)) # False

# and
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

# or
print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5> 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)