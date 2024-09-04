# 10828. 스택
# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

N = int(input().rstrip())

stack = []
for _ in range(N):
    command = input().rstrip().split()

    # push X: 정수 X를 stack에 넣는 연산
    if command[0] == 'push':
        X = int(command[1])
        stack.append(X)
    
    # pop: stack에 정수가 있는지 확인 후
    # 있다면 가장 위에 있는 정수를 빼고 출력,
    # 없다면 -1을 출력
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    # size: stack의 들어있는 정수의 개수를 출력
    elif command[0] == 'size':
        print(len(stack))
    
    # empty: stack에 정수가 있는지 확인 후
    # 없다면 1을 출력, 있다면 0을 출력
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    
    # top: stack에 정수가 있는지 확인 후
    # 있다면 가장 위에 있는 정수를 뺴고 출력 후 다시 삽입
    # 없다면 -1을 출력
    elif command[0] == 'top':
        if stack:
            x = stack.pop()
            print(x)
            stack.append(x)
        else:
            print(-1)