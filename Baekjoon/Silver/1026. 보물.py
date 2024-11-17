# 1026. 보물
# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

# A의 수와 B의 수를 곱한 값들을 더한 값 S가
# 최솟값이 되려면 A의 최솟값 x B의 최댓값이여야 하므로
# A는 오름차순으로, B는 내림차순으로 정렬
A.sort()
B.sort(reverse=True)

# A의 수와 B의 수를
# 곱한 값을 더해 S를 계산
S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)