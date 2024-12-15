# 1303. 전쟁 - 전투
# https://www.acmicpc.net/problem/1303

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 같은 팀의 병사들끼리 얼마나 모여있는지
# 탐색하고자 bfs 구현
def bfs(i, j, color):
    qu = collections.deque()

    # 초기값 설정
    cnt = 1
    qu.append((i, j))
    area[i][j] = 0

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 기준이 되는 병사로부터 상하좌우 확인
        for d in delta:
            ni, nj = si+d[0], sj+d[1]

            # 만약 확인하는 곳이 전쟁터 범위 내에 있고
            # 병사가 같은 팀이라면 cnt에 1을 더하고
            # qu에 해당 좌표를 삽입해 뭉쳐있음을 표시
            # 중복탐색을 방지하고자 해당 값을 0으로 갱신
            if 0<=ni<M and 0<=nj<N and area[ni][nj] == color:
                cnt += 1
                qu.append((ni, nj))
                area[ni][nj] = 0

    # 뭉쳐있는 인원수를 제곱해
    # 낼 수 있는 위력을 반환
    return cnt**2


N, M = map(int, input().rstrip().split())
area = [list(input().rstrip()) for _ in range(M)]

w_cnt = 0
b_cnt = 0

for i in range(M):
    for j in range(N):
        
        # 병사가 입고 있는 옷에 따라
        # 아군, 적군을 구별해 위력을 계산
        if area[i][j] == 'W':
            w_cnt += bfs(i, j, 'W')
        elif area[i][j] == 'B':
            b_cnt += bfs(i, j, 'B')

# 아군 병사의 위력의 합과
# 적국 병사의 위력의 합 출력
print(w_cnt, b_cnt)