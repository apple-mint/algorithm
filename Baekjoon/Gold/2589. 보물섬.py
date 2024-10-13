# 2589. 보물섬
# https://www.acmicpc.net/problem/2589

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 서로 간 최단 거리로 이동하는 데 있어
# 가장 긴 시간이 걸리는 육지 두 곳을
# 찾기 위해 bfs 함수 구현
def bfs(i, j):
    qu = collections.deque()

    # 방문 표시와 최단 거리를 동시에
    # 나타내기 위해 -1을 초기값으로 설정
    visited = [[-1]*w for _ in range(h)]

    qu.append((i, j))
    visited[i][j] = 0

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 상하좌우로 이웃한 곳으로 이동
        for d in delta:
            ni = si+d[0]
            nj = sj+d[1]

            # 만약 이동한 곳이 지도 범위 내에 있고
            # 아직 방문하지 않은 육지라면
            # 시작점으로부터 다른 육지가 얼마나 멀리 있는지
            # 확인하기 위해 새로운 값을 qu에 삽입하고 visited 값 갱신
            if 0<=ni<h and 0<=nj<w:
                if visited[ni][nj] == -1 and info[ni][nj] == 'L':
                    qu.append((ni, nj))
                    visited[ni][nj] = visited[si][sj] + 1

    # 시작점에서 방문할 수 있는 곳 중
    # 가장 먼 곳으로 가는 데에 얼마나 걸리는지를 확인
    maxx = 0
    for i in range(h):
        cnt = max(visited[i])
        maxx = max(maxx, cnt)

    # 시작점에서 가장 먼 곳을 최단 거리로
    # 이동하는 데에 걸린 시간을 반환
    return maxx


h, w = map(int, input().rstrip().split())
info = [list(input().rstrip()) for _ in range(h)]

# 각 칸마다 가장 멀리 떨어진 육지를 찾고
# 여태까지 탐색한 것들 중에서 가장 멀리 떨어졌는지 확인
# 그렇다면 보물이 묻혀 있는 곳이므로 cnt 갱신
cnt = -1
for i in range(h):
    for j in range(w):
        if info[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))

print(cnt)