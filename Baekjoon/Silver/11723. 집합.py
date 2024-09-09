# 11723. 집합
# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline

M = int(input().rstrip())

S = set()
for _ in range(M):
    command = input().rstrip().split()

    # add x: 정수 x를 S에 추가하는 연산
    # set의 경우 중복을 허용하지 않으므로
    # x가 이미 있는지 따로 연산을 하지 않고 추가
    if command[0] == 'add':
        x = int(command[1])
        S.add(x)
    
    # remove x: 정수 x가 S에 있는지 확인 후
    # 있다면 제거, 없으면 해당 연산 무시
    elif command[0] == 'remove':
        x = int(command[1])
        if x in S:
            S.remove(x)

    # check x: 정수 x가 S에 있는지 확인 후
    # 있다면 1을 출력, 없다면 0을 출력
    elif command[0] == 'check':
        x = int(command[1])
        if x in S:
            print(1)
        else:
            print(0)

    # toggle x: 정수 x가 S에 있는지 확인 후
    # 있다면 x를 제거, 없다면 x를 추가
    elif command[0] == 'toggle':
        x = int(command[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    # all: S = {1, 2, ..., 20} 으로 바꾸기 위해
    # 정수 1~20까지 S에 추가
    elif command[0] == 'all':
        for x in range(1, 21):
            S.add(x)
    
    # empty: S를 공집합으로 바꾸는 연산
    elif command[0] == 'empty':
        S.clear()