# 7569. 토마토
# https://www.acmicpc.net/problem/7569

import sys, collections
input = sys.stdin.readline

delta = [
    (-1, 0, 0), (1, 0, 0),
    (0, -1, 0), (0, 1, 0),
    (0, 0, -1), (0, 0, 1)
]

# 인접한 곳을 살펴보며 최소 일수를
# 구해야 하므로 bfs 구현
def bfs(tomatoes):

    # 익은 토마토를 시작점으로 삼음
    qu = collections.deque(tomatoes)
    
    # bfs 시작
    while qu:

        # 높이, 앞뒤, 좌우로 접근할 수 있는 좌표와
        # 최소 며칠이 걸리는지 표시할 변수를 qu에서 꺼냄
        sk, si, sj, cnt = qu.popleft()
        
        # 하나의 토마토에 인접한 곳을 방문
        for d in delta:
            nk, ni, nj = sk+d[0], si+d[1], sj+d[2]

            # 방문한 곳이 범위 내에 있고
            # 익지 않은 토마토가 있는 곳이라면
            # 해당 토마토를 qu에 삽입해 이를 기준으로
            # 다른 인접한 토마토를 익힐 수 있는지 확인하고
            # 토마토의 상태를 익은 것으로 값을 갱신
            if 0<=nk<H and 0<=ni<N and 0<=nj<M:
                if not boxes[nk][ni][nj]:
                    qu.append((nk, ni, nj, cnt+1))
                    boxes[nk][ni][nj] = 1

    # bfs가 끝난 뒤 모든 토마토가 익었는지 확인
    for i in range(N):
        for j in range(M):
            for k in range(H):

                # 만약 익지 않은 토마토가 있다면 -1 반환
                if not boxes[k][i][j]:
                    return -1

    # 모든 토마토가 익어있는 상태라면
    # 모든 토마토가 익는 데에 걸린 일수 반환
    return cnt


M, N, H = map(int, input().rstrip().split())

# 3차원 배열을 구현하기 위해
# 해당 2차원 배열을 리스트에 요소로 삽입
# boxes[높이][앞뒤][좌우]로 접근할 수 있음
boxes = []
for _ in range(H):
    boxes.append([list(map(int, input().rstrip().split())) for _ in range(N)])

# 익은 토마토가 어디 있는지 찾으며
# 해당 위치와 익는 데에 걸린 일수를 저장
tomatoes = []
for i in range(N):
    for j in range(M):
        for k in range(H):
            if boxes[k][i][j] == 1:
                tomatoes.append((k, i, j, 0))

# 익은 토마토를 기준으로 모든 토마토가
# 익으려면 최소 며칠이 걸리는지 탐색
cnt = bfs(tomatoes)

# 구한 값을 출력
print(cnt)