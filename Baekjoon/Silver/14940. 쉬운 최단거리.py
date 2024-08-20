# 14940. 쉬운 최단거리
# https://www.acmicpc.net/problem/14940

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(gi, gj):
    qu = collections.deque()

    # 원래 갈 수 있는 땅인 부분 중
    # 도달할 수 없는 위치를 -1로 표시하기 위해
    # 다음과 같이 visited 초기값 설정
    visited = [[-1]*m for _ in range(n)]

    # 원래 갈 수 없는 땅일 경우
    # 해당 위치의 visited 값을 0으로 변경
    for i in range(n):
        for j in range(m):
            if not ground[i][j]:
                visited[i][j] = 0

    qu.append((gi, gj))
    visited[gi][gj] = 0

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        for de in delta:
            ni = si+de[0]
            nj = sj+de[1]

            # 시작점에서 가로와 세로로 움직였을 때
            # 지도의 범위 내에 있고 아직 방문한 적이 없는 곳이라면
            # qu에 해당 위치를 새로운 시작점으로 삽입해주고
            # 목표지점에서 시작점으로 오는 데에 걸린 거리 + 1을
            # 해당 위치의 visited 값으로 변경해 거리를 기록
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == -1:
                qu.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1
    
    # 기록한 거리를 반환
    return visited


n, m = map(int, input().rstrip().split())
ground = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 목표지점에서 모든 지점에 대한
# 목표지점까지의 거리를 bfs를 통해 구함
for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            ans = bfs(i, j)
            break

# 모든 지점에 대한 목표지점까지의 거리를
# 주어진 출력예시에 따라 출력
for i in range(n):
    print(*ans[i])