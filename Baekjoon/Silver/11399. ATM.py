# 11399. ATM
# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

N = int(input().rstrip())
P = list(map(int, input().rstrip().split()))

# 돈을 인출하는 데에 걸리는 시간의 합이 최소가 되려면
# 걸리는 시간이 작은 순서대로 돈을 인출하면 되므로 정렬
P.sort()

# 첫번째로 선 사람이 걸린 시간을 초기값으로 설정
cnt = P[0]

# 이전 사람이 걸린 시간 + 현재 인출하는 데에 걸리는 시간
# 각 사람이 인출하는데 걸리는 시간 계산 후 그 값을 갱신
for i in range(1, N):
    cnt += P[i]
    P[i] = cnt

# 각자 얼마나 걸렸는지 시간이 기록되어 있으므로
# 그 전체의 합을 구해 출력
print(sum(P))