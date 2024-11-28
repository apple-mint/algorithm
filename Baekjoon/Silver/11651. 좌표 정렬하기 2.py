# 11651. 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

N = int(input().rstrip())

dots = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    dots.append((x, y))

# lambda 함수를 활용해 1. y좌표가 증가하는 순,
# 2. y좌표가 같다면 x좌표가 증가하는 순으로 정렬
dots.sort(key=lambda x:(x[1], x[0]))
for i in range(N):
    print(*dots[i])