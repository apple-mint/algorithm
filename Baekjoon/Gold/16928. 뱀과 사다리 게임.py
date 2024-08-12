# 16928. 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928

import sys, collections
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 1~100칸이므로 번호를 맞추기 위해 101칸으로 만듦
board = [0] * 101

# 사다리과 뱀의 정보를 board 해당 번호 인덱스에 저장
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    board[u] = v

# bfs로 최소 몇 번 굴려야 하는지 찾기 위해 deque 사용
qu = collections.deque()

# board와 마찬가지로 번호를 맞추기 위해 101칸으로 만듦
visited = [0] * 101

# 1번 칸에서 bfs 시작
qu.append(1)
while qu:
    x = qu.popleft()

    # 만약 100번 칸에 도착했을 경우 종료
    if x == 100:
        break

    # 1~6까지 수가 적혀 있는 주사위를 굴려 이동
    for n in range(1, 7):
        m = x+n

        # 만약 주사위를 굴려 이동한 칸이
        # 보드판 범위 내에 있고 처음 방문한 곳이라면
        # 이전 최솟값 + 1을 저장해 방문표시
        if m <= 100 and not visited[m]:
            visited[m] = visited[x] + 1

            # 해당 칸이 0이 아니라면 사다리 또는 뱀으로
            # 해당 칸에 있는 값으로 이동
            if board[m]:
                m = board[m]

                # 만약 이동한 칸에 처음 방문한 곳이라면
                # 이전 최솟값 + 1을 저장해 방문표시
                if not visited[m]:
                    visited[m] = visited[x] + 1
            
            # 사다리 또는 뱀으로 이동했다면 최종으로 도착한 곳에서,
            # 혹은 둘다 없었다면 처음 도착한 곳에서
            # 다시 주사위를 굴려 이동하므로 qu에 삽입
            qu.append(m)

# 100번 칸에 도착하기 위한 최솟값 출력
print(visited[100])