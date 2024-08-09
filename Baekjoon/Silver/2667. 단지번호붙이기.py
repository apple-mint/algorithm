# 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 상하좌우로 연결된 집들을 단지라고 정의하므로
# 이를 위해 bfs 탐색 시작
def bfs(i, j):
    qu = collections.deque()

    cnt = 1
    qu.append((i, j))
    area[i][j] = 0

    # bfs 탐색 시작
    while qu:
        si, sj = qu.popleft()

        # 시작점에서 상하좌우로 탐색했을 때
        for de in delta:
            ni = si + de[0]
            nj = sj + de[1]

            # 이동한 곳이 지도 범위 내에 있고
            # 아직 단지로 포함되지 않은 집이라면
            # 집의 수인 cnt에 1를 더하고
            # 단지로 포함된 집이라는 뜻으로 0으로 값을 갱신
            if 0<=ni<N and 0<=nj<N and area[ni][nj]:
                cnt += 1
                qu.append((ni, nj))
                area[ni][nj] = 0

    # 단지로 포함된 집의 수를 반환
    return cnt


N = int(input().rstrip())
area = [list(map(int, input().rstrip())) for _ in range(N)]

# 각 단지에 속하는 집 수를 담을 ans
ans = []
for i in range(N):
    for j in range(N):

        # 만약 단지로 포함되지 않은 집이 있다면
        # 해당 집을 시작점으로 bfs 탐색
        if area[i][j]:
            ans.append(bfs(i, j))

# 각각 단지수, 각 단지에 속하는 집 수를
# 문제에 제시된 조건에 따라 출력
print(len(ans))
print(*sorted(ans), sep='\n')