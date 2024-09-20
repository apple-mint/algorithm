# 18404. 현명한 나이트
# https://www.acmicpc.net/problem/18404

import sys, collections
input = sys.stdin.readline

# 나이트가 이동할 수 있는 경우의 수
delta = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

N, M = map(int, input().rstrip().split())

board = [[0]*N for _ in range(N)]
X, Y = map(int, input().rstrip().split())

# 상대편 말을 잡기 위한 최소 이동 수를
# 정보가 주어졌던 순서에 맞게 출력하기 위해
# 해당 순번으로 체스판인 board에 상대편 말의 위치를 표시하고
# key를 순번으로 가지도록 opponent에 저장
opponent = {}
for i in range(1, M+1):
    A, B = map(int, input().rstrip().split())
    board[A-1][B-1] = i
    opponent[i] = 0

# 상대편 말을 몇 개 잡았는지를 기록하는 변수
cnt = 0

# bfs를 통해 최소 이동 수를 구하려 하므로
# popleft 메서드를 사용할 수 있는 deque 사용
qu = collections.deque()
visited = [[-1]*N for _ in range(N)]

# 현재 나이트의 위치를 qu에 삽입하고
# 해당 위치에 방문표시를 해 초기값 설정
qu.append((X-1, Y-1))
visited[X-1][Y-1] = 0

# bfs 시작
while qu:

    # 만약 상대편 말을 모두 잡았다면 탐색 종료
    if cnt == M:
        break
    
    # 현재 나이트의 위치에서
    # 이동할 수 있는 경우로 인접한 곳으로 이동
    x, y = qu.popleft()
    for d in delta:
        nx = x + d[0]
        ny = y + d[1]

        # 이동한 곳이 체스판 범위 내이고 방문한 적이 없다면 
        # 또다른 곳으로 이동하기 위해 qu에 해당 위치를 삽입하고
        # 여기까지 이동하는 데에 걸린 수에
        # 1을 더한 값으로 해당 위치에 방문표시를 해줌
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
            qu.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

            # 만약 이동한 곳에 상대편 말이 있을 경우
            # cnt에 1을 더해 상대편 말을 잡았음을 표시
            # opponent에서 해당 순번의 key를 찾고
            # 해당 key의 value로 여기까지 이동하는 데에 걸린 수를 저장
            if board[nx][ny]:
                cnt += 1
                opponent[board[nx][ny]] = visited[nx][ny]

# 상대편 말 정보가 주어졌던 순서에 맞게
# 최소 이동 수를 공백을 기준으로 출력
print(*opponent.values(), sep=' ')