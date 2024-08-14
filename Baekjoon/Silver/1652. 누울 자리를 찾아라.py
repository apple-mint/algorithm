# 1652. 누울 자리를 찾아라
# https://www.acmicpc.net/problem/1652

import sys
input = sys.stdin.readline

N = int(input().rstrip())
room = [list(input().rstrip()) for _ in range(N)]

# 가로줄 탐색
row = 0
for i in range(N):

    # 하나의 줄에 빈 칸이, 즉 '.'칸이
    # 얼마나 연속해서 있는지 확인하기 위한 변수
    cnt = 0
    for j in range(N):

        # 만약 빈 칸이라면 cnt에 1을 더해줌
        if room[i][j] == '.':
            cnt += 1

        # 만약 짐이 있는 곳이라면
        # 이전에 2칸 이상의 빈 칸이 존재했는지 확인하고
        # 그렇다면 row에 1을 추가하고 cnt를 초기화
        # 아니라면 row에 추가하지 않고 cnt만 초기화
        else:
            if cnt >= 2:
                row += 1
            cnt = 0
        
        # 해당 가로줄에 마지막 칸이 빈 칸인 경우
        # 2칸 이상의 빈 칸이 존재했는지 따로 확인할 수 없으므로
        # 마지막 칸일 경우 2칸 이상의 빈 칸이 존재했는지를 확인
        if j == N-1:
            if cnt >= 2:
                row += 1

# 가로줄과 동일한 방식으로 세로줄 탐색
col = 0
for j in range(N):
    cnt = 0
    for i in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col += 1
            cnt = 0
    
    if i == N-1:
        if cnt >= 2:
            col += 1

print(row, col)