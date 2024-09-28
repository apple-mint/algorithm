# 2304. 창고 다각형
# https://www.acmicpc.net/problem/2304

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 기둥의 왼쪽 면의 위치가 무작위로 주어지므로
# 시작점과 끝점을 알기 위해 초기값 설정
start_L, end_L = 1001, 0

# 지붕은 모든 기둥과 윗면 또는 옆면과 닿아야 하며
# 오목하게 들어간 부분이 없어야 하므로
# 가장 높은 곳을 기준으로 면적을 파악하기 위해
# 가장 높은 곳의 위치와 그 높이의 초기값 설정
max_L, max_H = 0, 0

columns = {}
for L in range(1, 1001):
    columns[L] = 0

# 각 기둥의 왼쪽 면의 위치에 따라 높이 기록
for _ in range(N):
    L, H = map(int, input().rstrip().split())
    columns[L] = H

    # 시작점인지 확인 후
    # 시작점이라면 그 값으로 갱신
    if L < start_L:
        start_L = L
    
    # 끝점인지 확인 후
    # 끝점이라면 그 값으로 갱신
    if L > end_L:
        end_L = L

    # 높이가 가장 높은지 확인 후
    # 그렇다면 그 위치와 그 높이를 갱신
    if H > max_H:
        max_L = L
        max_H = H

# 높이가 가장 높은 위치를 기준으로
# 창고 다각형의 면적을 구하므로
# 높이에 해당하는 값을 더해줌
ans = columns[max_L]

# 현재 위치에 도달하기 전
# 가장 기둥이 높은 곳의 위치
pre_L = 0

# 시작점에서 높이가 가장 높은 위치까지 탐색
for L in range(start_L, max_L):

    # 만약 시작점인 경우
    # ans에 해당 기둥의 높이를 더해주고
    # pre_L를 현재 위치로 갱신
    if L == start_L:
        ans += columns[L]
        pre_L = L

    # 이전 위치값이 있다면
    # 현재 위치의 높이와 이전 위치의 높이를 비교 후
    # 만약 현재 위치의 높이가 더 높다면
    # ans에 해당 기둥의 높이를 더해주고
    # pre_L를 현재 위치로 갱신
    else:
        if columns[L] > columns[pre_L]:
            ans += columns[L]
            pre_L = L

        # 그렇지 않다면 오목하게 들어간 부분이 없도록
        # ans에 이전에 가장 높은 기둥의 높이를 더해줌
        else:
            ans += columns[pre_L]

# 끝점에서 높이가 가장 높은 위치까지 탐색
# 면적을 계산하는 방법은 위와 동일
for L in range(end_L, max_L, -1):
    if L == end_L:
        ans += columns[L]
        pre_L = L

    else:
        if columns[L] > columns[pre_L]:
            ans += columns[L]
            pre_L = L
        else:
            ans += columns[pre_L]

# 구한 창고 다각형의 면적을 출력
print(ans)