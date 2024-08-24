# 11726. 2×n 타일링
# https://www.acmicpc.net/problem/11726

import sys
input = sys.stdin.readline

n = int(input().rstrip())
tile = [0, 1, 2]

for num in range(3, n+1):

    # 2xn 크기의 직사각형을 채우는 방법의 수는
    # 1. 이전 2xn 크기의 직사각형에서
    # 오른쪽에 2x1 타일을 붙인 경우,
    # 2. 그 타일을 붙였을 때 2x2가 된다면
    # 해당 2x1 타일 2개를 붙여 90도로 돌리는 경우의 합이고
    # 해당 수를 10,007로 나눈 나머지를 출력해야 함

    # 따라서 아래와 같은 점화식을 쓸 수 있으며
    # n까지 그 수를 계산해서 tile에 삽입
    tile.append((tile[num-1]+tile[num-2])%10007)

print(tile[n])