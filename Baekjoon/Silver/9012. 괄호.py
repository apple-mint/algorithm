# 9012. 괄호
# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    PS = input().rstrip()

    stack = []
    is_VPS = False

    for i in range(len(PS)):

        # '('일 경우 stack에 삽입
        if PS[i] == '(':
            stack.append(PS[i])
        
        # ')'일 경우 '('이 있어야 하므로
        # stack이 비어 있다면 VPS이 아니므로 종료,
        # '('이 있다면 짝을 찾았으므로 하나를 제거
        else:
            if not stack:
                break
            else:
                stack.pop()

    # 모든 탐색을 마쳤을 때 stack이 비어 있다면
    # 모든 괄호가 짝이 지어진 것이므로 VPS
    # is_VPS를 True로 값 갱신
    else:
        if not stack:
            is_VPS = True

    if is_VPS:
        print('YES')
    else:
        print('NO')