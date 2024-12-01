# 1654. 랜선 자르기
# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

K, N = map(int, input().rstrip().split())

cables = []
for _ in range(K):
    cables.append(int(input().rstrip()))

# 잘린 랜선의 길이가 될 수 있는
# 최솟값, 최댓값 설정
minn = 1
maxx = max(cables)

# 이분탐색 시작
while minn <= maxx:
    
    cnt = 0
    
    # 최대 랜선의 길이를 해당 값이 될 수 있는
    # 최솟값과 최댓값의 중간값으로 설정했을 때
    # 나오는 랜선의 개수를 구함
    mid = (minn+maxx)//2
    for cable in cables:
        cnt += cable//mid

    # 만약 그 랜선의 개수가 N개보다 크거나 같으면
    # 랜선의 길이가 더 길어도 되므로
    # minn을 mid에 1을 더한 값으로 갱신
    if cnt >= N:
        minn = mid+1

    # 그렇지 않다면 랜선의 길이가 더 짧아야 하므로
    # maxx를 mid에 1을 뺀 값으로 갱신
    else:
        maxx = mid-1

# N개를 만들 수 있는 랜선의 최대 길이 출력
print(maxx)