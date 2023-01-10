print('보라돌이','뚜비','나나','뽀')

def add(*numbers):
    
    result = 0
    for n in numbers:
        result += n
    return result

print(add(1,2,3,10,23))

def movie(**kwargs):
    print(type(kwargs))

print(movie(name='더 글로리', writer='김은숙'))