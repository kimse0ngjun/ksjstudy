# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "얼어붙은 건틀릿"
print(sentence2)
sentence3 = """
나는 김성준 낭랑 24세 입니다.
내일 10시에 아침 수업을 들을 계획입니다.
"""
print(sentence3)

# 슬라이싱
wonseok = "990708-1327401"

print("성별 : " + wonseok[7])
print("연 : " + wonseok[0:2]) # 0 ~ 2 직전까지
print("월 : " + wonseok[2:4])
print("일 : " + wonseok[4:6]) 

print("생년월일 : " + wonseok[:6]) # 처음부터 6 직전까지
print("뒤 7자리: " + wonseok[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + wonseok[-7:]) 
# 맨 뒤에서 7번째부터 끝까지

# 문자열 처리함수
python = "Python is Interesting"
print(python.lower()) # 소문자로 변환(lower)
print(python.upper()) # 대문자로 변환(upper)
print(python[0].isupper()) # 0번째의 인덱스의 글자가 대문자 맞나? = True
print(len(python)) # python 전체 길이
print(python.replace("python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # Java가 들어갔는지 찾아줌(없을 땐 -1로 출력)
# print(python.index("Java")) 
# Java가 들어갔는지 인덱스로 찾아줌(실제로 값이 없을 경우(java) 오류가 생겨 밑에 print문이 있어도 멈춰버림)
print("hi")
print(python.count("n")) # n이 몇번 나오나?