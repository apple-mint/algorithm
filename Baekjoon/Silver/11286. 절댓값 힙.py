# 11286. 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for _ in range(N):
    x = int(input().rstrip())

    # x가 정수일 경우 배열에 x 값을 추가
    # 절댓값이 가장 작은 값을 출력하는데
    # 해당 값이 여러 개일 경우 가장 작은 수를 출력해야 하므로
    # 배열에 x의 절댓값, x 값 순으로 묶어 추가
    if x:
        heapq.heappush(arr, (abs(x), x))

    # x가 정수가 아니면 x는 0이므로
    # 배열 상태에 따라 적절한 값 출력
    else:

        # 만약 배열에 값이 있는 경우
        # 위 조건에 따라 해당하는 가장 작은 값을 출력
        if arr:
            print(heapq.heappop(arr)[1])

        # 만약 배열이 비어 있는 경우 0을 출력
        else:
            print(0)