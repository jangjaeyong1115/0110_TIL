a,b = input("문자열과 알파벳을 공백으로 구분해서 입력해주세요").split()
cnt = 0
for i in a:
    if i == b:
        cnt += 1
    
print(cnt)