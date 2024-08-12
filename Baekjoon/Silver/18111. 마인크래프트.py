# 18111. 마인크래프트
# https://www.acmicpc.net/problem/18111

import sys, collections
input = sys.stdin.readline

N, M, B = map(int, input().rstrip().split())
ground = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 가장 높은 높이의 땅과 가장 낮은 높이의 땅을 찾기 위해
# 다음과 같이 초기값 설정
maxx = -1
minn = 257

# minn부터 maxx까지 가능한 땅의 높이를
# 빠르게 탐색하기 위해 딕셔너리 사용
# 0으로 초기값을 설정하기 위해 defaultdict 사용
height = collections.defaultdict(int)

# 해당하는 땅의 높이가 몇 개 있는지를 탐색하며
# 탐색 범위를 줄이기 위해 최댓값, 최솟값도 같이 탐색
# M, N의 범위는 0부터 500까지이고 땅의 높이의 범위는 0부터 256이므로
# 땅의 높이가 몇 개 있는지 따로 계산하지 않고
# 집터를 전부 탐색할 경우 시간 초과 발생
for i in range(N):
    for j in range(M):
        height[ground[i][j]] += 1
        
        if ground[i][j] > maxx:
            maxx = ground[i][j]

        if ground[i][j] < minn:
            minn = ground[i][j]

# 땅을 고르는 데 걸리는 시간과
# 땅의 높이를 구하기 위한 초기값 설정
ans = [float('inf'), -1]

# 만약 최댓값과 최솟값이 같은 경우
# 모든 땅의 높이가 같으므로 다음과 같이 값 설정
if maxx == minn:
    ans = [0, maxx]

# 최솟값과 최댓값 사이로
# 맞출 땅의 높이를 정해 땅을 고르기 시작
for n in range(minn, maxx+1):
    cnt = 0
    block = B

    for h, c in height.items():

        # 만약 다듬어야 할 땅의 높이가 맞출 땅의 높이보다 큰 경우,
        # 블록을 제거한 만큼 2를 곱해 cnt에 더해주고
        # 블록을 제거한 만큼 block에 더해줌
        if h > n:
            cnt += 2 * c * (h-n)
            block += c * (h-n)

        # 만약 다듬어야 할 땅의 높이가 맞출 땅의 높이보다 작거나 같은 경우,
        # 블록을 놓은 만큼 cnt에 더해주고 block에 빼줌
        else:
            cnt += c * (n-h)
            block -= c * (n-h)
    
    # 만약 블록의 수가 음수가 아니고
    # 걸린 시간이 여태까지 나온 값보다 작거나 같은 경우
    # 현재 시간과 현재 높이로 값 갱신
    if block >= 0 and cnt <= ans[0]:
        ans[0] = cnt
        ans[1] = n

print(*ans, sep=' ')