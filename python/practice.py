# 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print()

# 문자형
print('아이')
print("학교")
print("우하하ㅋ")
print("ㅋ"*9) # 문자열 + 정수

print()

# 참 / 거짓 boolean 자료형
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True) # True의 반대 -> False
print(False) # False의 반대 -> True

print()

# 애완동물 소개(변수)
animal = "강아지"
name = "마루쉐"
age = 1
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "이름은" + name + " 이예요")
# print(name + "는" + str(age) + "이며," + hobby + "을 좋아해요") 
print(name, "는", str(age), "이며,", hobby, "을 좋아해요") # ,로 쓰게되면 정수형, 불리안 변수를 그대로 쓸 수 있다.
print(name + "는 어른일까요?" + str(is_adult))
 
print("우리집 강아지 이름은 마루이예요")
print("마루는 1살이며, 산책을 좋아해요")
print("마루는 어른일까요? False")
