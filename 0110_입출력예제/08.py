# 테스트 케이스마다 입력 값을 그대로 출력하세요.
5 # 테스트 케이스 수
#1 38 108 29 3 2 39
#1 9 12 3 5 1
#28 39 1 20 9 1
#34 5 6 8
#9 3 2 10 1 2 4


T = int(input())

for t in range(1, T+1):
    # 여러개의 공백으로 구분된 정수 입력 받기
    numbers = list(map(int,input().split()))

    print(numbers)
