# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "자바")
# profile("김성준", 24, "파이썬")
# \t = 탭 문자(데이터를 정렬, 가독성을 높히기 위해 사용)

# profile을 호출했을 때 age=17, main_lang=파이썬 나오도록 하는 코드
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))
    
profile("유재석")
profile("김성준")
