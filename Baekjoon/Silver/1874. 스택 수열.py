# 1874. 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []

# 만약 수열을 만드는 것이 불가능한 경우
# 이후 불필요한 연산을 하지 않도록 변수 설정
is_possible = True

# 1이상 n이하의 정수를 push하기 위한 초기값
x = 1

ans = []
for _ in range(n):
    num = int(input().rstrip())
    tmp = 0

    if is_possible:

        # 주어진 정수가 stack에 한번 삽입되어 있어야 하므로
        # 초기값을 이용하여 stack에 순차적으로 삽입
        while x <= num:
            stack.append(x)
            ans.append('+')
            x += 1

        # stack에 남아 있는 것이 있을 때 pop연산 진행
        # 주어진 정수와 비교할 초기값을 설정하기 위해
        # 맨 뒤에 있는 값을 제거하고 다시 삽입
        if stack:
            y = stack.pop()
            stack.append(y)

            # 주어진 정수가 나올 때까지 pop 연산 진행
            while y >= num:
                y = stack.pop()
                ans.append('-')

                # 주어진 정수가 나왔다면
                # 수열을 만드는 것이 가능한지 아닌지
                # 판별하기 위해 tmp에 현재 값을 갱신하고 종료
                if y == num:
                    tmp = y
                    break
        
        # 만약 마지막으로 pop 연산이 된 값이
        # 주어진 정수와 일치하지 않을 경우
        # 해당 수열은 불가능한 경우이므로 False로 값 갱신
        if tmp != num:
            is_possible = False

# 수열을 만드는 것이 가능한 경우
# 필요한 연산을 한줄에 하나씩 출력
if is_possible:
    print(*ans, sep='\n')

# 불가능한 경우 NO 출력
else:
    print('NO')