# 7562. 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys, collections
input = sys.stdin.readline

# 나이트가 움직일 수 있는 범위
delta = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# 나이트가 최소 몇 번만에 현재 있는 칸에서
# 이동하려고 하는 칸에 갈 수 있는지
# 확인하고자 bfs를 함수로 구현
def bfs(ci, cj, di, dj):

    qu = collections.deque()
    visited = [[-1]*I for _ in range(I)]

    # 나이트의 시작점을 초기값으로 설정
    qu.append((ci, cj))
    visited[ci][cj] = 0

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 만약 이동하려고 하는 칸에 도착했을 경우
        # 이동하는 데에 걸린 횟수를 반환
        if si == di and sj == dj:
            return visited[di][dj]
        
        # 나이트가 현재 있는 칸에서
        # 움직일 수 있는 범위만큼 이동
        for d in delta:
            mi = si+d[0]
            mj = sj+d[1]

            # 만약 움직인 칸이 체스판 범위 내에 있고
            # 한번도 방문하지 않았다면
            # 해당 칸을 최소 횟수로 방문한 것이므로
            # qu에 해당 좌표를 삽입하고 visited 표시를 해줌
            if 0<=mi<I and 0<=mj<I and visited[mi][mj] == -1:
                qu.append((mi, mj))
                visited[mi][mj] = visited[si][sj] + 1


T = int(input().rstrip())

# 주어진 테스트 케이스만큼
# 나이트가 최소 몇 번만에 이동할 수 있을지를 탐색
for _ in range(T):
    I = int(input().rstrip())
    ci, cj = map(int, input().rstrip().split())
    di, dj = map(int, input().rstrip().split())

    # bfs 함수로 구하고자 하는 값을 찾고 출력
    print(bfs(ci, cj, di, dj))