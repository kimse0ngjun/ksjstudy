# 리스트 [] (하나의 연속적인 공간에 묶는 것)

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에서 탐
subway.append("하하")
print(subway)

# 정형돈를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # (인덱스 숫자, 객체)
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 (pop)
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능(sort())
num_list = [4,2,3,5,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 기능 (reverse())
num_list.reverse()
print(num_list)

# 모두 지우기 (clear())
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 !
num_list = [5,3,4,2,1]
mix_list = ["정형돈", 20, True]

# 리스트 확장 (extend())
num_list.extend(mix_list)
print(num_list)
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


#