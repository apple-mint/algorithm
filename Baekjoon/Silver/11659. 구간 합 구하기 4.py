# 11659. 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

# 시작점인 0부터 인덱스 번호에 해당되는 수까지의 합
# i, j번째를 맞추고 용이한 누적합 계산을 위해 0부터 시작
total = [0, nums[0]]

# 주어진 수들의 누적합 계산
for i in range(1, N):
    total.append(total[i]+nums[i])
    
# i번째 수부터 j번째 수까지의
# 구간합 계산 및 출력
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(total[j]-total[i-1])