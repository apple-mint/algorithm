# 10845. 큐
# https://www.acmicpc.net/problem/10845

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

queue = collections.deque()
for _ in range(N):
    command = input().rstrip().split()

    # push X: 정수 X를 queue에 넣는 연산
    if command[0] == 'push':
        X = int(command[1])
        queue.append(X)
    
    # pop: queue에 정수가 있는지 확인 후
    # 있다면 가장 앞에 있는 정수를 빼고 출력,
    # 없다면 -1을 출력
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    # size: queue의 들어있는 정수의 개수를 출력
    elif command[0] == 'size':
        print(len(queue))
    
    # empty: queue에 정수가 있는지 확인 후
    # 없다면 1을 출력, 있다면 0을 출력
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    
    # front: queue에 정수가 있는지 확인 후
    # 있다면 가장 앞에 있는 정수를 뺴고 출력 후
    # appendleft 메서드를 통해 그 자리에 다시 삽입
    # 없다면 -1을 출력
    elif command[0] == 'front':
        if queue:
            x = queue.popleft()
            print(x)
            queue.appendleft(x)
        else:
            print(-1)

    # back: queue에 정수가 있는지 확인 후
    # 있다면 가장 뒤에 있는 정수를 뺴고 출력 후
    # append 메서드를 통해 그 자리에 다시 삽입
    # 없다면 -1을 출력
    elif command[0] == 'back':
        if queue:
            x = queue.pop()
            print(x)
            queue.append(x)
        else:
            print(-1)