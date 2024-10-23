# 1189. 컴백홈
# https://www.acmicpc.net/problem/1189

import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# K번만큼 이동하는 하나의 경로로 갔을 때
# 집에 도착할 수 있는지를 확인해야 하므로 dfs 함수 구현
def dfs(i, j, cnt):
    global ans
    
    # K번만큼 움직였을 때 집에 도착했는지에 따라
    # ans에 1을 더할 수 있도록 한 뒤 해당 경로 탐색 종료
    if cnt == K:
        if i == 0 and j == C-1:
            ans += 1
        return

    for d in delta:
        ni, nj = i+d[0], j+d[1]

        # 1. 이동한 곳이 맵 범위 내에 있고
        # 2. '.'으로 갈 수 있는 부분이며
        # 3. 아직 방문하지 않은 곳이면 그 곳으로 이동
        if 0<=ni<R and 0<=nj<C and info[ni][nj] == '.' and not visited[ni][nj]:
            
            # 해당 위치의 좌표에 방문표시를 하고
            # K번만큼 이동하기 위해 dfs 함수 호출
            visited[ni][nj] = 1
            dfs(ni, nj, cnt+1)

            # 다른 경로가 가능한지 탐색하고자
            # 방문표시를 초기화함
            visited[ni][nj] = 0


R, C, K = map(int, input().rstrip().split())
info = [list(input().rstrip()) for _ in range(R)]

ans = 0
visited  = [[0]*C for _ in range(R)]

# 시작점인 곳에 방문표시를 해주고 dfs 함수를 호출해
# 집에 갈 수 있는 거리가 K인 가짓수를 구함
visited[R-1][0] = 1
dfs(R-1, 0, 1)

# 구한 값을 출력
print(ans)