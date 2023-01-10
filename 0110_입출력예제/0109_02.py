s = (input('문자열을 입력하세요 : '))

if s == " ": 
    print(0) 
else:
    text = s.split(" ")  
    for i in text: 
        if i == '': 
            text.remove('') 

    print(text.__len__())