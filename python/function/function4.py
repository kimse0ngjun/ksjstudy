# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("김성준", 25, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 24, "Kotlin", "Swift", "", "", "")

# 위의 코드는 할줄아는 lang이 늘게 되면 lang6, lang7 이런식으로 게속 추가해주어야함
# 이걸 보완한 코드가 가변인자
    
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
    
profile("김성준", 25, "Python", "Java", "C", "C++", "C#")
profile("김태호", 24, "Kotlin", "Swift")