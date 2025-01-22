# score.txt 파일을 만듦
# score_file = open("score.txt", "w", encoding="utf8") # w 쓰기 용도 = 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a = append 내용 추가
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close() # close()로 닫아줘야됨

# 1. 각각 하나씩 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")

# 2. 반복문 이용
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 3. 리스트 이용
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
    
score_file.close()