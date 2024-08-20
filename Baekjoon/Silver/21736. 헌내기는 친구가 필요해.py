# 21736. 헌내기는 친구가 필요해
# https://www.acmicpc.net/problem/21736

import sys, collections
input = sys.stdin.readline

# 도연이가 이동할 수 있는 방법
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# bfs로 도연이가 만날 수 있는 사람의 수를 구함
# 도연이가 있는 곳인 좌표를 받아 탐색 시작
def bfs(i, j):
    qu = collections.deque()
    visited = [[0]*M for _ in range(N)]

    qu.append((i, j))
    visited[i][j] = 1

    cnt = 0
    while qu:
        ii, ij = qu.popleft()

        for de in delta:
            mi, mj = ii+de[0], ij+de[1]

            # 이동할 수 있는 방법대로 움직였을 때
            # 이동한 곳이 캠퍼스 내에 있으면서 벽이 아니고
            # 방문하지 않은 곳이라면 새로운 시작점으로 삼음
            if 0<=mi<N and 0<=mj<M and campus[mi][mj]!='X' and not visited[mi][mj]:
                qu.append((mi, mj))
                visited[mi][mj] = 1

                # 만약 이동한 곳에 사람이 있다면
                # cnt에 1을 더해줌
                if campus[mi][mj] == 'P':
                    cnt += 1

    # 탐색을 종료했을 때 만약 cnt가 0이라면
    # 만날 수 있는 사람이 없는 것이므로 'TT' 출력
    if not cnt:
        return 'TT'
    
    # cnt가 0이 아니라면
    # 최소 한 명 이상의 사람을 만난 것이므로
    # 그 수를 출력
    else:
        return cnt


N, M = map(int, input().rstrip().split())
campus = [list(input().rstrip()) for _ in range(N)]

# 도연이가 있는 곳으로부터 bfs 시작
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            ans = bfs(i, j)

print(ans)