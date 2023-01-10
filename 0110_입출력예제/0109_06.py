list = []
result = 0
count = 1
a = int(input("양의 정수를 입력하세요 : "))
b = a
if b <= 0:
    print(-1)
else:
    while(1):
        if b < 10:
            break
        else:
            count += 1
            b = b//10
print(count)

for i in range(count,-1,-1):
    c = a//(10**(i))
    list.append(c)
    a = a - c*(10**(i))

for j in list:
    result += j

print(result)