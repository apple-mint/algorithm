# 1331. 나이트 투어
# https://www.acmicpc.net/problem/1331

import sys
input = sys.stdin.readline

# 나이트가 이동할 수 있는 경우의 수
delta = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# 1. 나이트가 이동할 수 있는 경우의 수 중 하나로 이동하면서,
# 2. 6x6 체스판 위를 모두 방문했는지를 확인하는 변수
is_valid = True

# 6x6 체스판 위에 모두 방문해야 하므로
# 방문 표시를 위한 visited 설정
visited = [[0]*6 for _ in range(6)]

# si, sj: 나이트가 처음 방문한 곳
# pi, pj: 나이트가 직전에 방문한 곳
si, sj = 0, 0
pi, pj = 0, 0

# 나이트가 방문한 순서대로 탐색 시작
for i in range(36):
    knight = input().rstrip()

    # 맨 좌측 위 행과 열 좌표가 (0, 0)임을 고려해
    # 해당 행과 열 좌표 값에 맞춰 변환
    vi, vj = ord(knight[0])-65, 6-int(knight[1])

    # 만약 첫 번째 방문일 경우,
    # si, sj에 해당 위치를 저장하고 방문 표시
    if not i:
        si, sj = vi, vj
        visited[vi][vj] = 1

    else:
        # 만약 이전에 방문한 곳이 있다면
        # 나이트가 이동할 수 있는 경우 중에서
        # 해당 위치로 이동할 수 있는지를 확인
        # 이동할 수 있다면 for문을 종료하고
        # 그 다음 어디를 방문했는지 확인
        for de in delta:
            if vi == pi+de[0] and vj == pj+de[1]:
                visited[vi][vj] = 1
                break

        # 도중에 for문이 종료되지 않았다면
        # 나이트가 이동할 수 있는 경우로는 갈 수 없는 곳이므로
        # is_valid를 False로 갱신
        else:
            is_valid = False

        # 만약 마지막 방문이라면 해당 좌표에서
        # 나이트가 이동할 수 있는 경우 중에서
        # 처음 방문한 곳으로 갈 수 있는지를 확인
        if i == 35:
            for de in delta:
                if si == vi+de[0] and sj == vj+de[1]:
                    visited[vi][vj] = 1
                    break
            
            # 도중에 for문이 종료되지 않았다면
            # 나이트가 이동할 수 있는 경우로는 갈 수 없으므로
            # is_valid를 False로 갱신
            else:
                is_valid = False

            # 36칸 모두를 방문해야 하므로
            # 만약 1칸이라도 방문 표시가 되어 있지 않다면
            # is_valid를 False로 갱신
            for i in range(6):
                for j in range(6):
                    if not visited[i][j]:
                        is_valid = False

    # 다음 나이트가 방문한 곳과 비교할 수 있도록
    # 직전에 방문한 곳의 좌표 갱신
    pi, pj = vi, vj

# is_valid 값에 따라 정답 출력
if is_valid:
    print('Valid')
else:
    print('Invalid')