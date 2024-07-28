# 2178. 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().rstrip().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]

# 미로를 통과하는 데에 최소의 칸 수를 구해야 하므로
# bfs 탐색을 통해 visited에 방문 횟수를 저장하고
# 도착 위치인 (N, M)일 때 저장된 방문 횟수 출력 후 종료
qu = collections.deque()
visited = [[0] * M for _ in range(N)]

qu.append((0, 0))
visited[0][0] = 1

while qu:
    i, j = qu.popleft()

    if i == N-1 and j == M-1:
        print(visited[N-1][M-1])
        break
    
    for de in delta:
        ni = i + de[0]
        nj = j + de[1]

        if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and miro[ni][nj]:
            qu.append((ni, nj))
            visited[ni][nj] += visited[i][j] + 1