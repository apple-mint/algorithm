# 14719. 빗물
# https://www.acmicpc.net/problem/14719

import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
block = list(map(int, input().rstrip().split()))

# 가장 높이가 높은 블록을 기준으로
# 두 구역으로 나눠 빗물이 얼마나 고이는지 계산
# 가장 높이가 높은 블록이 여러 개 있다면
# 가장 첫번째로 나오는 인덱스를 기준으로 삼음
idx = block.index(max(block))

# 고이는 빗물의 총량
rainwater = 0

# 블록 내부 공간마다 고이는 빗물의 양
cnt = 0

# 왼쪽에서부터 높이가 가장 높은 블록까지
# 빗물이 얼마나 고이는지 계산
for i in range(idx+1):

    # 시작점 설정
    if not i:
        start = i

    else:
        # 만약 시작점이 현재 블록의 높이보다 높을 경우
        # 빗물이 고일 수 있으므로 그 차만큼 계산
        if block[start] > block[i]:
            cnt += block[start] - block[i]

        # 만약 그렇지 않다면
        # 하나의 블록 내부 공간이 끝난 것이므로
        # 여태까지 고인 빗물의 양을 총합에 더해주고 초기화한 뒤
        # 시작점을 해당 블록으로 설정
        else:
            rainwater += cnt
            cnt = 0
            start = i

# 오른쪽에서부터 높이가 가장 높은 블록까지
# 빗물이 얼마나 고이는지 위와 동일한 방식으로 계산
for i in range(W-1, idx-1, -1):
    if i == W-1:
        start = i

    else:
        if block[start] > block[i]:
            cnt += block[start] - block[i]
        else:
            rainwater += cnt
            cnt = 0
            start = i

print(rainwater)