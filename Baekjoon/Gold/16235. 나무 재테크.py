# 16235. 나무 재테크
# https://www.acmicpc.net/problem/16235

import sys, collections
input = sys.stdin.readline

# python3으로는 시간초과,
# PyPy3는 통과된 코드

delta = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1),
    (0, 1), (1, -1), (1, 0), (1, 1)
]

# for문을 최소한으로 사용하기 위해
# 서로 영향이 없는 봄, 여름, 겨울 연산을 한번에 진행
def spring_summer_winter():
    for r in range(N):
        for c in range(N):
            for _ in range(len(alive[r][c])):

                # 계절마다 일어나는 사건을 수행할 수 있는지
                # 오름차순대로 각 나무를 확인
                tree = alive[r][c].popleft()

                # 봄에는 각 나무가 자신의 나이만큼 양분을 먹고
                # 나이가 1씩 증가하므로 해당 땅의 양분이
                # 자신의 나이보다 크거나 같은지 확인
                if ground[r][c] >= tree:

                    # 만약 그렇다면 먹은 양분만큼 양분을 빼주고
                    # 나이를 1 증가시킨 뒤 나무 목록에 다시 추가
                    # 오름차순을 유지하기 위해 맨 뒤에 삽입
                    ground[r][c] -= tree
                    tree += 1
                    alive[r][c].append(tree)

                # 그렇지 않다면 나무는 죽으므로 그대로 제거
                # 여름에 죽은 나무의 나이를 2로 나눈 값의 정수값이
                # 양분이 되므로 해당 값을 구해 해당되는 dead 좌표값에 갱신
                else:
                    nutrient[r][c] += tree//2

            # 살아있는 나무 목록을 모두 확인한 뒤
            # 여름에 양분이 된 값과 겨울에 추가하는 양분 값을 더해
            # 해당 땅에 양분을 추가하고 여름에 양분이 된 값 초기화
            ground[r][c] += nutrient[r][c] + A[r][c]
            nutrient[r][c] = 0
    
    return


# 가을에 각 나무들이 번식할 수 있는지 확인
def autumn():
    for r in range(N):
        for c in range(N):
            for i in range(len(alive[r][c])):

                # 여기서는 값 변경 없이 확인만 할 것이므로
                # popleft 메서드를 사용하지 않고
                # 인덱스를 사용해 나무의 나이 값을 변수에 할당
                tree = alive[r][c][i]

                # 만약 나무의 나이가 5의 배수일 경우
                # 번식할 수 있는 나무이므로
                # 인접한 8개의 칸이 땅을 벗어나지 않는지 확인
                if not tree%5:
                    for de in delta:
                        nr = r+de[0]
                        nc = c+de[1]

                        # 만약 땅을 벗어나지 않는다면
                        # 인접한 칸에 나이가 1인 나무를 추가
                        # 오름차순을 유지하기 위해 맨 앞에 삽입
                        if 0<=nr<N and 0<=nc<N:
                            alive[nr][nc].appendleft(1)
    
    return


N, M, K = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 양분 초기값 설정
ground = [[5]*N for _ in range(N)]

# 각 땅마다 살아있는 나무 목록을 저장할 배열
# 오름차순을 유지하고자 popleft, appendleft
# 연산이 가능한 deque 사용
alive = [[collections.deque() for _ in range(N)] for _ in range(N)]

# 상도가 심은 나무 정보를 나무 목록에 표시
for _ in range(M):
    x, y, z = map(int, input().rstrip().split())
    alive[x-1][y-1].append(z)

# 봄에 죽은 나무가 양분으로 변한 값을 저장할 배열
nutrient = [[0]*N for _ in range(N)]

# K년만큼 사계절을 보냄
for _ in range(K):
    spring_summer_winter()
    autumn()

# K년이 지난 후 살아있는 나무의 개수 확인
cnt = 0
for r in range(N):
    for c in range(N):
        cnt += len(alive[r][c])

# 살아있는 나무의 개수 출력
print(cnt)