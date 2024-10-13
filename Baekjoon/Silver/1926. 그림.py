# 1926. 그림
# https://www.acmicpc.net/problem/1926

import sys, collections
input = sys.stdin.readline

# 가로나 세로로 연결되었는지
# 확인하기 위한 상하좌우 좌표값
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 가로나 세로로 연결된 것을
# 하나의 그림이라고 했을 때
# 그 그림의 넓이를 구하기 위해 bfs 함수 구현
def bfs(i, j):

    # 그림의 넓이
    cnt = 1

    # bfs 구현을 위해 deque 사용
    qu = collections.deque()

    # bfs를 위한 초기값 설정
    # 별도의 visited 없이 picture에 바로 표시
    qu.append((i, j))
    picture[i][j] = 0

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 상하좌우로 이동
        for d in delta:
            ni = si+d[0]
            nj = sj+d[1]

            # 이동한 곳이 그림 내에 있고 색칠이 된 부분이라면
            # 그림의 넓이에 1을 추가하고
            # 이동한 곳의 i, j 값을 qu에 삽입한 뒤
            # 색칠이 안된 부분으로 변경해 방문표시를 해줌
            if 0<=ni<n and 0<=nj<m and picture[ni][nj]:
                cnt += 1
                qu.append((ni, nj))
                picture[ni][nj] = 0

    # 그림의 넓이를 반환
    return cnt


n, m = map(int, input().rstrip().split())
picture = [list(map(int, input().rstrip().split())) for _ in range(n)]

cnt = 0
maxx = 0

# 도화지 전체를 살펴보면서 색칠이 된 부분이 있을 경우
# 그림이 하나 나온 것이므로 cnt에 1을 추가
# 해당 그림의 넓이가 최댓값인지 확인하고
# 만약 최댓값이라면 maxx 값 갱신
for i in range(n):
    for j in range(m):
        if picture[i][j]:
            cnt += 1
            maxx = max(maxx, bfs(i, j))

# 출력 예시에 따라 그림의 개수,
# 가장 넓은 그림의 넓이를 출력
print(cnt)
print(maxx)