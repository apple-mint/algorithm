# 1920. 수 찾기
# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

N = int(input().rstrip())
n_nums = list(map(int, input().rstrip().split()))

# 모든 정수의 범위가 매우 크므로
# 빠르게 존재 여부를 알 수 있도록 딕셔너리 활용
A = {}
for n in n_nums:
    A[n] = 1

M = int(input().rstrip())
m_nums = list(map(int, input().rstrip().split()))

# M개의 수들이 A 안에 존재하는지 확인
# 존재하면 1을, 아니라면 0을 출력
for m in m_nums:
    if A.get(m):
        print(1)
    else:
        print(0)