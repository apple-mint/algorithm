# 2468. 안전 영역
# https://www.acmicpc.net/problem/2468

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 물이 잠기지 않는 지점들이 상하좌우로
# 붙어 있는 영역을 찾아야 하므로 bfs 사용
def bfs(i, j, rain):
    qu = collections.deque()

    qu.append((i, j))
    visited[i][j] = 1

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        for d in delta:
            ni = si + d[0]
            nj = sj + d[1]

            # 시작점으로부터 상하좌우로 이동한 곳이
            # (1) 범위 내에 있으면서, (2) 이전에 방문한 적이 없고,
            # (3) 해당 지점의 높이가 내린 비의 양보다 클 경우
            # 이곳으로부터 상하좌우로 붙어 있는 영역을 새로 찾기 위해
            # qu에 해당 좌표를 삽입하고 visited에 방문 표시를 해줌
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                if area[ni][nj] > rain:
                    qu.append((ni, nj))
                    visited[ni][nj] = 1

    # 연결된 영역 수와 상관없이
    # 항상 하나의 영역을 찾을 수 있으므로
    # 그 수로 1를 반환
    return 1


N = int(input().rstrip())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 장마철에 내리는 비의 양이 제시되지 않았으므로
# 모든 곳이 잠기기 직전까지의 안전한 영역을
# 확인하기 위해 최대 높이를 구함
maxx = 0
for i in range(N):
    maxx = max(maxx, max(area[i]))

# 아무 지역도 물에 잠기지 않을 수 있으므로,
# 즉 비가 1보다 적게 내릴 수 있으므로
# 다음과 같이 비의 양의 범위를 설정
ans = 0
for rain in range(maxx):
    cnt = 0

    # 비의 양이 달라질 때마다 visited 초기화
    visited = [[0]*N for _ in range(N)]
    
    # 물에 잠기지 않는 영역이면서
    # 방문한 적이 없는 곳인 경우
    # 해당 위치를 기준으로 안전한 영역을 탐색
    for i in range(N):
        for j in range(N):
            if area[i][j] > rain and not visited[i][j]:
                cnt += bfs(i, j, rain)

    # 찾은 안전한 영역의 수가
    # 최대값인지 확인 후 최댓값이라면 값 갱신
    ans = max(ans, cnt)

print(ans)