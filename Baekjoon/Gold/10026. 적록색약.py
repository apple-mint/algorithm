# 10026. 적록색약
# https://www.acmicpc.net/problem/10026

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 적록색약이 아닌 사람의 구역 탐색
def RGB(i, j, color):

    qu = collections.deque()
    qu.append((i, j))
    RGB_visited[i][j] = 1

    while qu:
        si, sj = qu.popleft()

        # 같은 색상이 상하좌우로 인접해 있는지 확인하기 위해
        # 시작점으로부터 상하좌우로 탐색
        for d in delta:
            ni, nj = si+d[0], sj+d[1]

            # 1. 상하좌우로 이동한 값이 그림 범위 내에 있고,
            # 2. 다른 구역에 포함되어있지 않으며,
            # 3. 색이 같을 경우,
            # 같은 구역이라고 할 수 있으므로
            # 새로운 시작점으로 만들어 탐색을 이어나감
            if 0<=ni<N and 0<=nj<N and not RGB_visited[ni][nj] and picture[ni][nj] == color:
                qu.append((ni, nj))
                RGB_visited[ni][nj] = 1

    # 상하좌우로 인접해 있는 구역 하나를 탐색 완료
    return 1


# 적록색약인 사람의 구역 탐색
def RB(i, j, color):

    qu = collections.deque()
    qu.append((i, j))
    RB_visited[i][j] = 1

    while qu:
        si, sj = qu.popleft()

        for d in delta:
            ni, nj = si+d[0], sj+d[1]

            # 적록색약은 빨간색과 초록색의 차이를 구분하지 못하므로
            # 색이 빨간색과 초록색인 경우, 파란색인 경우를 나눠 탐색
            if 0<=ni<N and 0<=nj<N and not RB_visited[ni][nj]:

                if color == 'R' or color == 'G':
                    if picture[ni][nj] == 'R' or picture[ni][nj] == 'G':
                        qu.append((ni, nj))
                        RB_visited[ni][nj] = 1

                else:
                    if picture[ni][nj] == color:
                        qu.append((ni, nj))
                        RB_visited[ni][nj] = 1

    return 1


N = int(input().rstrip())
picture = [list(input().rstrip()) for _ in range(N)]

# 탐색했는지 여부를 표시해주는 배열 생성
RGB_visited = [[0] * N for _ in range(N)]
RB_visited = [[0] * N for _ in range(N)]

RGB_cnt = 0
RB_cnt = 0

# 탐색하지 않은 곳을 시작점으로 구역 탐색
# 한 번 탐색할 때마다 해당 색과 같은 곳을
# 모두 탐색하므로 결과값은 항상 하나의 구역으로 나옴
for i in range(N):
    for j in range(N):
        if not RGB_visited[i][j]:
            RGB_cnt += RGB(i, j, picture[i][j])

        if not RB_visited[i][j]:
            RB_cnt += RB(i, j, picture[i][j])

# 구역의 수를 출력 양식에 맞게 출력
print(RGB_cnt, RB_cnt)