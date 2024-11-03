# 4108. 지뢰찾기
# https://www.acmicpc.net/problem/4108

import sys
input = sys.stdin.readline

# 하나의 칸에서 인접한 상, 하, 좌, 우,
# 4개의 대각선칸으로 이동하는 좌표모음
delta = [
    (-1, -1), (-1, 0), (-1, 1), 
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# 해당 칸과 인접한 곳에 지뢰가 있는지 찾는 함수
def search(r, c):
    cnt = 0

    # 해당 칸과 인접한 곳으로 이동
    for d in delta:
        nr, nc = r+d[0], c+d[1]

        # 만약 이동한 곳이 범위 내에 있고
        # 해당 칸에 지뢰가 있다면 cnt에 1을 더해줌
        if 0<=nr<R and 0<=nc<C and area[nr][nc] == '*':
            cnt += 1

    # 인접한 곳에 있는
    # 지뢰의 개수를 반환
    return cnt


# 여러 개의 테스트 케이스를 받기 위해 while문 사용
while True:
    R, C = map(int, input().rstrip().split())

    # 0 0이 입력되면 종료
    if not R and not C:
        break

    area = [list(input().rstrip()) for _ in range(R)]

    # 지뢰밭의 모든 칸을 탐색
    # 만약 하나의 칸이 빈 공간이라면
    # search 함수를 호출해 인접한 곳에 있는
    # 지뢰의 개수를 구하고 그 값을 해당 칸에 갱신
    for r in range(R):
        for c in range(C):
            if area[r][c] == '.':
                area[r][c] = search(r, c)

    # 출력 예시에 따라 출력
    for r in range(R):
        print(*area[r], sep='')