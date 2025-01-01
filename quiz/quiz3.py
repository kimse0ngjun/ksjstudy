# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호 {1} 입니다.".format(url, password))