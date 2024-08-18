# 1003. 피보나치 함수
# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

# fibonacci[0] = 0, fibonacci[1] = 1이고
# fibonacci[N] = fibonacci[N-1] + fibonacci[N-2]인 피보나치 수
fibonacci = [0, 1, 1, 2]

# N의 범위가 0부터 40까지이므로
# 40까지 피보나치 수를 만들어줌
for n in range(3, 40):
    fibonacci.append(fibonacci[n]+fibonacci[n-1])

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())

    # 피보나치 함수가 호출되었을 때
    # fibonacci(0), fibonacci(1)가 호출되는 수를 구해야 함
    # fibonacci(0)일 경우 fibonacci(0)이 1번만 호출되므로
    # N이 0일 경우 다음과 같이 출력
    if not N:
        print(1, 0)

    # 계산 결과 fibonacci(0)은 fibonacci[N-1],
    # fibonacci(1)은 fibonacci[N]와 동일하므로 다음과 같이 출력
    else:
        print(fibonacci[N-1], fibonacci[N])