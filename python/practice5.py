# 조건문
# weather = "미세먼지"
# weather = input("오늘 날씨는 어때요?: ") # 날씨 입력하는 ㅗ

# if weather == "비":
#     print("우산 챙기세요")
# elif weather == "미세먼지":
#     print("마스크 챙기세용")
# else:
#     print("준비물 필요없어요")
    
    
# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("더워요. 집에 있으세요")
# elif 10 <= temp and temp < 30:
#     print("날씨가 좋아요")
# elif 0 <= temp and temp < 10:
#     print("후드 입으세요")
# else:
#     print("패딩 입으세요")
    
# 반복문
for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no)) 
# 리스트 내에 값들을 하나씩 돌아가면서 waiting_no 변수에 적용시키는 것

# randrange()
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
    
starbucks = ["배영진", "토르", "라이언킹"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    
## 문자열 포멧
# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # %d = 정수
print("나는 %s을 좋아해요." % '파이썬') # %s = 문자
print("Apple은 %c로 시작해요" % "A") 
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨강", age = 20))

# 방법 4
age = 24
color = "blue"
print("나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자

# \n: 줄바꿈
print("배가 아프다\n기침이 나온다.")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩" 입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \ (\하나로 url을 쓰게 되면 오류남)
print("C:\\Users\tjdwn\ksjstudy\python\practice5.p")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
#