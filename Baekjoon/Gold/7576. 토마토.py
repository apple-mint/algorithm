# 7576. 토마토
# https://www.acmicpc.net/problem/7576

import sys, collections
input = sys.stdin.readline

# 앞, 뒤, 왼쪽, 오른쪽 방향
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 하나의 토마토에 인접한 네 방향을 확인하고
# 모든 토마토가 익는 데에 걸리는
# 최솟값을 구해야 하므로 bfs 구현
def bfs(tomatoes, cnt):

    # popleft 메서드를 사용하기 위해
    # 익은 토마토들의 정보가 담긴 tomatoes를
    # list에서 deque로 형태를 바꿔 사용
    qu = collections.deque(tomatoes)

    # 익은 토마토가 익지 않은 토마토에
    # 영향을 주는지 탐색 시작
    while qu:

        # si, sj: 익은 토마토의 좌표
        # day: 해당 토마토가 익은 시점
        si, sj, day = qu.popleft()

        # 익은 토마토의 좌표를 기준으로
        # 앞, 뒤, 왼쪽, 오른쪽 방향으로 인접한 곳으로 이동
        for de in delta:
            ni = si + de[0]
            nj = sj + de[1]

            # 만약 인접한 곳이 범위 내에 있고
            # 그곳에 익지 않은 토마토가 있다면 해당 토마토는 익게 됨
            if 0<=ni<N and 0<=nj<M and not boxes[ni][nj]:

                # cnt에서 1을 빼주고 boxes 값을 갱신해
                # 해당 좌표에 있는 토마토가 익은 토마토임을 표시
                cnt -= 1
                boxes[ni][nj] = 1

                # day에 1을 더해 해당 토마토가 익은 시점을 기록
                ans = day+1

                # 새롭게 익은 토마토가 다른 익지 않은 토마토에
                # 영향을 줄 수 있는지 탐색하기 위해
                # 관련 정보를 묶어 qu에 삽입
                qu.append((ni, nj, ans))

    # 탐색이 끝났을 때 익지 않은 토마토가 없다면
    # 토마토가 모두 익을 때까지 걸린 일수 ans 반환
    if not cnt:
        return ans
    
    # 익지 않은 토마토의 수가 남아 있다면
    # 토마토가 모두 익지는 못하는 상황이므로 -1 반환
    else:
        return -1
    

M, N = map(int, input().rstrip().split())
boxes = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 익은 토마토들의 정보를 담을 리스트
tomatoes = []

# 익지 않은 토마토의 수
cnt = 0

for i in range(N):
    for j in range(M):

        # 익은 토마토의 경우 익지 않은 토마토에
        # 영향을 줄 수 있는지 확인하기 위해
        # 해당 토마토의 위치 정보와
        # 익는 데에 걸린 일수인 0을 같이 묶어 삽입
        if boxes[i][j] == 1:
            tomatoes.append((i, j, 0))
        
        # 익지 않은 토마토일 경우
        # cnt에 1을 더해 그 수를 세줌
        elif not boxes[i][j]:
            cnt += 1

# 만약 익지 않은 토마토가 없다면 저장될 때부터
# 모든 토마토가 익어있는 상태이므로 0 출력
if not cnt:
    print(0)

# 익지 않은 토마토가 있다면
# bfs 함수 호출 및 그 결과 출력
else:
    print(bfs(tomatoes, cnt))