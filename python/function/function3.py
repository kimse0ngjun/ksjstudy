# 키워드값

def profile(name, age, main_lang):
    print(name,age, main_lang)

# 키워드를 설정해둔 값 그대로 호출받게 되어서, 순서를 섞어두어도 순서대로 호출됨
profile(name="김성준", main_lang="파이썬", age=25)
profile(main_lang="자바", age=25, name="정인호")
