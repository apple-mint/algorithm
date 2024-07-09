# 17836. 공주님을 구해라!
# https://www.acmicpc.net/problem/17836

import sys, collections
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 검이 있는지 없는지를 확인
def find_gramr():
    qu = collections.deque()
    visited = [[-1] * M for _ in range(N)]

    qu.append((0, 0))
    visited[0][0] = 0

    while qu:
        sx, sy = qu.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:

                if area[nx][ny] == 0:
                    qu.append((nx, ny))
                    visited[nx][ny] = visited[sx][sy] + 1

                elif area[nx][ny] == 2:
                    return (nx, ny, visited[sx][sy] + 1)

    return 0


# 검을 먼저 찾아서 공주에게 도달할 수 있는지를 확인
def bfs_gramr(x, y):
    qu = collections.deque()
    visited = [[-1] * M for _ in range(N)]

    qu.append((x, y))
    visited[x][y] = 0

    while qu:
        sx, sy = qu.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                qu.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1

    if 0 < visited[N-1][M-1] <= T:
        return visited[N-1][M-1]
    
    else:
        return 0


# 검 없이 공주에게 도달할 수 있는지를 확인
def bfs_without_gramr():
    qu = collections.deque()
    visited = [[-1] * M for _ in range(N)]

    qu.append((0, 0))
    visited[0][0] = 0

    while qu:
        sx, sy = qu.popleft()

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                if area[nx][ny] == 0:
                    qu.append((nx, ny))
                    visited[nx][ny] = visited[sx][sy] + 1

    if 0 < visited[N-1][M-1] <= T:
        return visited[N-1][M-1]
    
    else:
        return 0


N, M, T = map(int, input().rstrip().split())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

# yes_gramr: 검이 있는 경우
# no_gramr: 검이 없는 경우
yes_gramr = 0
no_gramr = 0

# 검이 있는지를 확인
is_gramr = find_gramr()

# 만약 검이 있다면 검을 찾고 공주에게 도달할 수 있는지 확인
if is_gramr:
    gx, gy, dis = is_gramr
    
    # 검을 찾는 데에 걸린 시간 + 공주에게 도달한 시간이
    # 제한 시간인 T 이내인지 확인
    if bfs_gramr(gx, gy):
        
        if bfs_gramr(gx, gy) + dis <= T:
            yes_gramr = bfs_gramr(gx, gy) + dis

# 검 없이 공주에게 도달할 수 있는지를 확인
no_gramr = bfs_without_gramr()

# 만약 두 경우 모두 공주에게 도달했다면 그 중 최단시간 출력
if no_gramr and yes_gramr:
    print(min(no_gramr, yes_gramr))

# 그렇지 않다면 둘 중 값이 존재하는 것을 출력하고
# 둘다 도달하지 못했다면 Fail 출력
else:
    if yes_gramr:
        print(yes_gramr)
    elif no_gramr:
        print(no_gramr)
    else:
        print('Fail')