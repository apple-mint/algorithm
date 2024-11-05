# 16948. 데스 나이트
# https://www.acmicpc.net/problem/16948

import sys, collections
input = sys.stdin.readline

delta = [
    (-2, -1), (-2, 1), (0, -2),
    (0, 2), (2, -1), (2, 1)
]

# 데스 나이트가 목적지로 이동하는
# 최소 이동 횟수를 구하기 위해 bfs 구현
def bfs(r, c):

    qu = collections.deque()

    # 이동할 수 없는 경우 -1을 출력하기 위해
    # 초기값을 -1로 설정
    visited = [[-1]*N for _ in range(N)]
    
    # 시작 초기값 설정
    qu.append((r, c))
    visited[r][c] = 0

    # bfs 시작
    while qu:
        sr, sc = qu.popleft()

        # 만약 이동한 칸이 목적지라면 bfs 종료
        if sr == r2 and sc == c2:
            break
        
        # 이동할 수 있는 경우의 수로 이동
        for d in delta:
            nr, nc = sr+d[0], sc+d[1]
            
            # 만약 이동한 곳이 체스판 범위 내에 있고
            # 아직 방문하지 않은 곳이라면
            # 해당 칸의 좌표를 qu에 삽입하고
            # 이전 이동 횟수에 1을 더한 값으로 방문 표시를 함
            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == -1:
                qu.append((nr, nc))
                visited[nr][nc] = visited[sr][sc] + 1

    # 목적지까지 오는 데에
    # 얼마만큼 이동했는지 그 횟수를 반환
    return visited[r2][c2]


N = int(input().rstrip())
r1, c1, r2, c2 = map(int, input().rstrip().split())

# bfs 함수 호출로 최소 이동 횟수를 구하고
# 반환된 최소 이동 횟수 출력
print(bfs(r1, c1))