# 11650. 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

N = int(input().rstrip())

dots = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    dots.append((x, y))

# 1. x좌표가 증가하는 순,
# 2. x좌표가 같다면 y좌표가 증가하는 순으로 정렬
# python의 sort는 첫번째부터 순차적으로
# 오름차순으로 정렬하므로 별도로 작성해줄 필요 없음
dots.sort()
for i in range(N):
    print(*dots[i])