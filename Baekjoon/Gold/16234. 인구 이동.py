# 16234. 인구 이동
# https://www.acmicpc.net/problem/16234

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 인접한 나라끼리 국경선을 열어 만들어진
# 하나의 연합의 좌표를 파악하기 위해 bfs 구현
def bfs(r, c):
    qu = collections.deque()

    qu.append((r, c))
    visited[r][c] = 1
    group = [(r, c)]

    # bfs 시작
    while qu:
        sr, sc = qu.popleft()

        # 시작점에서 상하좌우로 인접한 곳으로 이동
        for d in delta:
            nr, nc = sr+d[0], sc+d[1]

            # 이동한 곳이 땅 범위 내에 있고
            # 아직 국경선을 열 수 있는지 확인하지 않은 곳이라면
            # 시작점과 이동한 곳의 인구 차이가 L명 이상 R명 이하인지 확인
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if L<=abs(A[sr][sc]-A[nr][nc])<=R:

                    # 그렇다면 국경선을 열 수 있으므로
                    # 해당 좌표를 기준으로 탐색할 수 있도록 qu에 추가하고
                    # 중복해서 탐색하는 것을 방지하고자 방문표시를 하고
                    # group에 추가함으로써 연합에 포함시킴
                    qu.append((nr, nc))
                    visited[nr][nc] = 1
                    group.append((nr, nc))

    # 만들어진 연합 좌표 반환
    return group


N, L, R = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]

ans = 0

# 인구 이동 시작
while True:

    # 인구 이동이 발생하지 않을 경우
    # while문을 종료하기 위한 변수 초기값 설정
    stop = True

    # 연합으로 구성될 수 있는지 탐색 여부를
    # 확인하기 위한 2차원 배열 초기값 설정
    visited = [[0]*N for _ in range(N)]

    # 모든 땅을 시작점으로 삼고 해당 땅과
    # 인접한 나라와 국경선을 열 수 있는지
    # bfs 함수를 호출해 확인
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                group = bfs(r, c)

                # 만약 연합을 이루고 있는 칸의 개수가
                # 1 초과일 경우 국경선이 열렸다는 의미
                if len(group) > 1:

                    # 다음에도 인구 이동이 발생할지
                    # 계속 확인하고자 stop을 False로 갱신
                    stop = False

                    # 연합의 인구수를 더한 값을 
                    # 연합을 이루고 있는 칸의 개수로 나눠
                    # 연합을 이루고 있는 각 칸의 인구수를 구함
                    population = 0          
                    for gr, gc in group:
                        population += A[gr][gc]
                    population //= len(group)

                    # 구한 각 칸의 인구수로 갱신
                    for gr, gc in group:
                        A[gr][gc] = population

    # 만약 인구 이동이 발생하지 않았다면
    # 인구 이동은 끝났으므로 while문 종료
    if stop:
        break
    
    # 인구 이동이 하루 발생했으므로
    # ans에 1을 더해줌
    ans += 1

# 며칠 동안 인구 이동이 발생했는지를 출력
print(ans)