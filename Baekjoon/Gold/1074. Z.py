# 1074. Z
# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

ans = 0

# 한 변의 길이가 2**N인 정사각형을
# 한 변의 길이가 1이 될 때까지
# 4등분하면서 방문 순서를 구함
while N > 0:
    N -= 1

    # 4등분으로 나눠진 정사각형 한 변의 길이
    M = 2**N

    # 1. 4등분으로 쪼개졌을 때
    # 주어진 r행 c열이 어느 구역에 있는지 확인
    
    # 2. 그 행과 열이 있는 정사각형을 다시 4등분을 해야 하므로
    # 해당 구역 내에서의 행과 열의 위치를 구해 값을 갱신함
    
    # 3. Z모양으로 방문하므로
    # 각 구역의 왼쪽 상단 첫번째를 기준으로
    # 0, 1*(M**2), 2*(M**2), 2*(M**2)씩 방문순서가 커지므로
    # 해당 구역이 어디인지에 따라 적절한 값을 더해줌

    # 왼쪽 상단
    if 0 <= r < M and 0 <= c < M:
        pass

    # 오른쪽 상단
    elif 0 <= r < M and M <= c < 2*M:
        c -= M
        ans += (M**2)

    # 왼쪽 하단
    elif M <= r < 2*M and 0 <= c < M:
        r -= M
        ans += (M**2)*2

    # 오른쪽 하단
    else:
        r -= M
        c -= M
        ans += (M**2)*3

print(ans)