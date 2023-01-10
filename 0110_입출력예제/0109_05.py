list=[]
list = input("양의정수 3개를 띄어쓰기로 구분해서 입력하세요 : ").split()
for i in list:
    if i == list[len(list)-1]:
        print(i)
    else:    
        print(i,end="-")