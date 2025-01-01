# 1 ~ 11 까지 책을 읽어보도록 시키는 코드, absent(결석자)는 continue를 사용하여 번호가 없어도 반복되도록 실행
# no_book(책 없는 사람)은 책을 읽을 수 없으니, 수업을 끝내고(break 사용 -> 반복문을 끝냄) 교무실로 따라오라는 코드임

# for, continue
absent = [2,5] # 결석
no_book = [7] # 책을 깜빡함
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))