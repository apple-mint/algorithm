# 2583. 영역 구하기
# https://www.acmicpc.net/problem/2583

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 직사각형의 내부를 제외한 나머지 부분의
# 넓이를 구하기 위해 bfs 사용
def bfs(x, y):
    qu = collections.deque()

    # 초기값 설정
    cnt = 1
    qu.append((x, y))
    area[y][x] = 0
    
    # bfs 시작
    while qu:
        sx, sy = qu.popleft()

        # 시작점으로부터 상하좌우를 탐색
        for de in delta:
            nx, ny = sx+de[0], sy+de[1]

            # 만약 시작점으로부터 특정 방향으로 이동했을 때
            # 이동한 곳이 범위 내에 있고 직사각형의 내부가 아니라면
            # 넓이에 1을 추가하고 qu에 해당 좌표를 삽입한 뒤
            # 같은 영역을 다시 탐색하지 않도록 0으로 값을 갱신
            if 0<=nx<N and 0<=ny<M and area[ny][nx]:
                cnt += 1
                qu.append((nx, ny))
                area[ny][nx] = 0

    # 구한 넓이를 반환
    return cnt


M, N, K = map(int, input().rstrip().split())

area = [[1]*N for _ in range(M)]
for _ in range(K):
    lx, ly, rx, ry = map(int, input().rstrip().split())

    # 2차원 배열 인덱스와 x, y좌표는 서로 반대이므로
    # x, y순이 아닌 y, x로 접근해
    # 직사각형의 내부에 해당하는 값을 0으로 갱신
    for x in range(lx, rx):
        for y in range(ly, ry):
            area[y][x] = 0

answers = []
for x in range(N):
    for y in range(M):

        # 만약 직사각형의 내부가 아니라면
        # 해당 영역을 포함한 영역의 넓이를
        # bfs를 통해 계산하고 해당 값을 삽입해 저장
        if area[y][x]:
            answers.append(bfs(x, y))

# 출력 예시에 따라 몇 개의 분리된 영역으로 나눠지는지,
# 분리된 각 영역의 넓이가 얼마인지 오름차순으로 정렬
print(len(answers))
print(*sorted(answers))