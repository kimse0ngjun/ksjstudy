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
