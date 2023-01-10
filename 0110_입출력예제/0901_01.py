string = input("문자열을 입력하세요: ")
cnt = 0
if 'e' in string:
    for i in string:
        if i == 'e':
            print(cnt)
            break
        elif i != 'e':
            cnt += 1
else:
    print(-1)