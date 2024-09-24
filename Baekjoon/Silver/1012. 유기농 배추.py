# 1012. 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 상하좌우로 인접한 배추들을 하나로 보고
# 그 수만큼 배추흰지렁이를 구입하면 되므로
# bfs로 그 수를 찾는 함수를 구현
def bfs(i, j):
    qu = collections.deque()

    # bfs를 위한 초기값 설정
    qu.append((i, j))
    farm[i][j] = 0

    while qu:
        si, sj = qu.popleft()

        for de in delta:
            ni = si + de[0]
            nj = sj + de[1]

            # 만약 인접한 곳으로 이동했을 때
            # 그 곳이 범위 내에 있고 배추가 있다면
            # 그곳에서 인접한 곳에 또다른 배추가 있는지
            # 확인하기 위해 qu에 해당 좌표 삽입 후
            # 배추를 제거해 중복해서 세지 않도록 함
            if 0<=ni<N and 0<=nj<M and farm[ni][nj]:
                qu.append((ni, nj))
                farm[ni][nj] = 0

    # 인접한 배추들을 하나로 간주해 1을 반환
    return 1


T = int(input().rstrip())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split())

    farm = [[0]*M for _ in range(N)]

    # 배열 탐색 시 알고 있던 행과 열이 반대가 되므로
    # 이를 고려해 X, Y를 서로 바꿔서
    # 배추가 심어져 있는 위치를 표시
    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        farm[Y][X] = 1

    cnt = 0

    # 배추가 있는 곳을 시작점으로 bfs를 통해
    # 서로 인접해있는 배추들이 몇 군데 있는지 수를 세줌
    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                cnt += bfs(i, j)

    # 필요한 배추흰지렁이 수를 출력
    print(cnt)