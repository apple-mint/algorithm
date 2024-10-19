# 1245. 농장 관리
# https://www.acmicpc.net/problem/1245

import sys, collections
input = sys.stdin.readline

# 인접한 격자들을 살펴보기 위한 delta
delta = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

# 인접한 곳에 기준이 되는 높이보다 크거나
# 같은지 확인하기 위해 bfs 함수 구현
def bfs(i, j):
    qu = collections.deque()

    # 기준이 되는 높이보다 크거나 같은지
    # 확인했는지 여부를 살펴보는 visited
    visited = [[0]*M for _ in range(N)]

    # 산봉우리 후보 좌표
    check = []
    
    qu.append((i, j))
    visited[i][j] = 1
    check.append((i, j))

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 기준점에서 인접한 격자들로 이동
        for d in delta:
            ni, nj = si+d[0], sj+d[1]

            # 이동한 곳이 농장 범위 내에 있고
            # 아직 높이를 확인하지 않았다면 높이를 확인
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:

                # 만약 기준 높이보다 크다면
                # 산봉우리가 될 수 없으므로 0 반환
                if farm[ni][nj] > farm[i][j]:
                    return 0

                # 만약 기준 높이와 같다면
                # 해당 격자도 하나의 산봉우리로 포함되므로
                # 해당 격자를 기준으로 인접한 격자를
                # 확인하기 위해 qu에 해당 좌표를 삽입
                # 중복해서 해당 격자를 확인하는 것을
                # 방지하고자 visited에 방문표시를 하고
                # check에 해당 좌표를 삽입
                elif farm[ni][nj] == farm[i][j]:
                    qu.append((ni, nj))
                    visited[ni][nj] = 1
                    check.append((ni, nj))

    # 도중에 반환 없이 끝났다면
    # 산봉우리 후보 좌표를 mountain에 표시해
    # 실제 산봉우리가 있음을 표시
    for ci, cj in check:
        mountain[ci][cj] = 1

    # 센 하나의 산봉우리를 반환
    return 1


N, M = map(int, input().rstrip().split())
farm = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 산봉우리인지 아닌지 확인하는 좌표
mountain = [[0]*M for _ in range(N)]

cnt = 0

# 산봉우리인지 아닌지 확인했는지를 살펴보고
# 확인하지 않았다면 bfs를 통해
# 해당 좌표가 산봉우리가 될 수 있는지를 확인하고
# 그 결과값을 cnt에 더해 개수를 구해줌
for i in range(N):
    for j in range(M):
        if not mountain[i][j]:
            cnt += bfs(i, j)

# 산봉우리의 개수 출력
print(cnt)