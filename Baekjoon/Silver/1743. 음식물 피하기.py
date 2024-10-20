# 1743. 음식물 피하기
# https://www.acmicpc.net/problem/1743

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 기준점으로부터 인접한 곳에
# 음식물이 있는지 확인하고자 bfs 함수 구현
def bfs(i, j):
    qu = collections.deque()

    qu.append((i, j))
    way[i][j] = 0

    # 음식물의 크기 초기값 설정
    cnt = 1

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 기준점으로부터 상하좌우로 이동
        for d in delta:
            ni, nj = si+d[0], sj+d[1]

            # 이동한 곳이 통로 범위 내이고 음식물이 있다면
            # 음식물이 커지므로 cnt에 1을 더해줌
            # 해당 좌표를 기준점으로 탐색을 하기 위해
            # qu에 해당 좌표를 삽입하고
            # 중복으로 탐색하는 것을 방지하고자 음식물을 제거함
            if 0<=ni<N and 0<=nj<M and way[ni][nj]:
                cnt += 1
                qu.append((ni, nj))
                way[ni][nj] = 0

    # 구한 음식물의 크기를 반환
    return cnt


N, M, K = map(int, input().rstrip().split())

# 음식물이 어디에 떨어졌는지 표시
way = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().rstrip().split())
    way[r-1][c-1] = 1

ans = 0

# 음식물이 떨어졌는지 통로 전체를 탐색
# 만약 음식물이 있다면 인접한 곳에도
# 음식물이 있어 커졌는지 확인하기 위해 bfs 함수 실행
for i in range(N):
    for j in range(M):
        if way[i][j]:
            cnt = bfs(i, j)

            # 구한 음식물의 크기가 가장 큰지 확인하고
            # 가장 크다면 ans를 해당 값으로 갱신
            ans = max(ans, cnt)

# 가장 큰 음식물의 크기 출력
print(ans)