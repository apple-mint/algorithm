# 14502. 연구소
# https://www.acmicpc.net/problem/14502

import sys, collections, itertools, copy
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# bfs를 활용해 현재 바이러스가 있는 위치에서
# 상하좌우로 인접한 칸으로 바이러스를 퍼트리는 함수
def bfs(i, j, lab):
    qu = collections.deque()

    # 초기 바이러스 좌표값 삽입
    qu.append((i, j))

    while qu:
        si, sj = qu.popleft()

        # 시작점에서 상하좌우로 인접한 곳으로 이동
        for de in delta:
            ni = si + de[0]
            nj = sj + de[1]

            # 만약 이동한 곳이 연구소 범위 내에 있고
            # 바이러스가 퍼질 수 있는 빈칸이라면
            # 해당 위치에서 또 바이러스를 퍼트리기 위해
            # 해당 좌표값을 qu에 삽입하고 해당 좌표값에 바이러스 표시
            if 0<=ni<N and 0<=nj<M and not lab[ni][nj]:
                qu.append((ni, nj))
                lab[ni][nj] = 2

    return


N, M = map(int, input().rstrip().split())
lab = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 새로운 벽을 세울 수 있는 빈 칸 i, j좌표
combis = []

# 바이러스의 i, j 좌표
virus = []

# 벽은 빈 칸에 세울 수 있고 빈칸은 0으로 표시,
# 바이러스는 2로 표시되어 있으므로
# 연구소 전체를 탐색하며 해당 값을 찾아
# 해당 좌표 위치를 알맞게 삽입
for i in range(N):
    for j in range(M):
        if not lab[i][j]:
            combis.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

# 바이러스가 퍼질 수 없는 안전 영역의 최대 크기
ans = 0

# combinations과 빈 칸의 좌표들을 활용해
# 새로 세울 3개의 벽 좌표값들의 조합을 만들고 리스트로 변환
combis = list(itertools.combinations(combis, 3))

# 모든 조합의 경우에서 하나의 경우의 수를 선택
for combi in combis:

    # 입력받은 값이 변형되지 않도록
    # deepcopy를 활용해 연구소 전체를 복사
    new_lab = copy.deepcopy(lab)

    # 가져온 하나의 경우의 수에 담긴 i, j를 활용해
    # 복사한 연구소 i, j 좌표에 해당하는 곳에 벽을 세워줌
    for c in range(3):
        new_lab[combi[c][0]][combi[c][1]] = 1

    # 초기 바이러스가 있는 곳에서부터 확산 시작
    for vi in virus:
        bfs(vi[0], vi[1], new_lab)

    # 바이러스 확산 후 안전 영역 수를 확인
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not new_lab[i][j]:
                cnt += 1

    # 만약 이번 안전 영역의 크기가
    # 그 전보다 크다면 해당 값으로 ans 갱신
    if cnt > ans:
        ans = cnt

print(ans)