# 10866. 덱
# https://www.acmicpc.net/problem/10866

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

deque = collections.deque()
for _ in range(N):
    command = input().rstrip().split()

    # push_front X: 정수 X를 deque 앞에 넣는 연산
    if command[0] == 'push_front':
        X = int(command[1])
        deque.appendleft(X)

    # push_back X: 정수 X를 deque 뒤에 넣는 연산
    elif command[0] == 'push_back':
        X = int(command[1])
        deque.append(X)
    
    # pop_front: deque에 정수가 있는지 확인 후
    # 있다면 가장 앞에 있는 정수를 빼고 출력,
    # 없다면 -1을 출력
    elif command[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)

    # pop_back: deque에 정수가 있는지 확인 후
    # 있다면 가장 뒤에 있는 정수를 빼고 출력,
    # 없다면 -1을 출력
    elif command[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)

    # size: deque에 들어있는 정수의 개수를 출력
    elif command[0] == 'size':
        print(len(deque))
    
    # empty: deque에 정수가 있는지 확인 후
    # 없다면 1을 출력, 있다면 0을 출력
    elif command[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    
    # front: deque에 정수가 있는지 확인 후
    # 있다면 가장 앞에 있는 정수를 출력,
    # 없다면 -1을 출력
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)

    # back: deque에 정수가 있는지 확인 후
    # 있다면 가장 뒤에 있는 정수를 출력,
    # 없다면 -1을 출력
    elif command[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)