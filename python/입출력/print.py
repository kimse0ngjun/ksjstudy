# # end="?" -> 뒤에 있는 문장이 한줄로 나오게 됨
# print("Python", "Java", sep=",", end="?") 

# print("무엇이 더 재밌을까요?")

# import sys 
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩": 60}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust: 수치만큼 띄어쓰기 해주는 코드
    
# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # zfill: 값이 없는 값을 0으로 채워주는 코드
    
# answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
# print("입력하신 값은" + answer + "입니다.") # 입력한 내용이 입력되었을 때 무조건 문자열 형태로 저장이 됨됨