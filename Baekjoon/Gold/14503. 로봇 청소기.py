# 14503. 로봇 청소기
# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

cnt = 0
while True:

    # 현재 칸이 아직 청소되지 않은 경우
    # 현재 칸을 청소하고 cnt에 1을 더해줌
    if not area[r][c]:
        cnt += 1
        area[r][c] = 99

    # 현재 칸 주변 4칸 중
    # 청소되지 않은 빈 칸이 있는지 탐색
    for _ in range(4):

        # 반시계 방향으로 90도씩 회전하며
        # 앞쪽 칸이 청소되지 않은 빈 칸인지 확인
        d = (d+3) % 4
        nr = r + delta[d][0]
        nc = c + delta[d][1]

        # 만약 청소되지 않은 빈칸일 경우
        # 한 칸 전진하고 해당 칸을 청소하기 위해 처음으로 돌아감
        if not area[nr][nc]:
            r = nr
            c = nc
            break
    
    else:
        # 현재 칸 주변 4칸을 모두 청소해
        # 청소하지 않은 빈 칸이 없는 경우
        # 바라보는 방향을 유지한 채 한 칸 후진할 수 있는지 확인
        r += delta[d-2][0]
        c += delta[d-2][1]

        # 후진할 수 없다면 작동을 멈추고
        # 후진할 수 있다면 처음으로 돌아감
        if area[r][c] == 1:
            break

print(cnt)