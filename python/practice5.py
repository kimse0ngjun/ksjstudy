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
    