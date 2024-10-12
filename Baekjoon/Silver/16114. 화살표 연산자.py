# 16114. 화살표 연산자
# https://www.acmicpc.net/problem/16114

import sys
input = sys.stdin.readline

X, N = map(int, input().rstrip().split())

# N이 0일 경우 X와 0의 대소관계를 비교하는 식이 됨
# 프로그램은 X의 값이 0보다 크지 않을 때 종료되므로
# X가 0보다 작거나 같다면 프로그램이 종료되어 0을,
# 아니라면 프로그램이 종료되지 않으므로 INFINITE 출력
if not N:
    if X <= 0:
        print(0)
    else:
        print('INFINITE')

# N이 1일 경우 -X와 0의 대소관계를 비교하는 식이 됨
# 따라서 X가 0보다 크거나 같다면 프로그램이 종료되어 0을,
# 아니라면 프로그램이 종료되지 않으므로 INFINITE 출력
elif N == 1:
    if X >= 0:
        print(0)
    else:
        print('INFINITE')

# N이 1을 제외한 홀수일 경우 화살표의 길이가 하나 남아
# 감소 연산자가 -X에 적용된 형태가 됨
# 이는 컴파일에 실패하는 경우이므로 ERROR 출력
elif N % 2:
    print('ERROR')

# N이 짝수일 경우 프로그램이 정상적으로 종료됨
# 따라서 while문을 통해 프로그램 동작을 구현
else:
    cnt = 0
    while True:

        # 화살표의 길이를 두 개씩 끊어
        # 하나의 감소 연산자로 계산하므로
        # 계산된 값만큼 X 값을 감소시킴
        X -= N//2

        # 만약 X의 값이 0보다 크지 않다면
        # 프로그램을 종료
        if X <= 0:
            break

        # X의 값을 출력하므로
        # cnt에 1를 더해 그 수를 세줌
        cnt += 1

    # 몇 개가 출력되는지 그 수를 출력
    print(cnt)