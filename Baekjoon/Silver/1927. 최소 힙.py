# 1927. 최소 힙
# https://www.acmicpc.net/problem/1927

import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for _ in range(N):
    x = int(input().rstrip())

    # x가 자연수일 경우 배열에 x 값을 추가
    if x:
        heapq.heappush(arr, x)

    # x가 자연수가 아니면 x는 0이므로
    # 배열 상태에 따라 적절한 값 출력
    else:

        # 만약 배열에 값이 있는 경우
        # 배열에서 가장 작은 값 출력
        if arr:
            print(heapq.heappop(arr))

        # 만약 배열이 비어 있는 경우 0을 출력
        else:
            print(0)