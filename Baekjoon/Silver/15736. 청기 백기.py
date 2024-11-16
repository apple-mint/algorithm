# 15736. 청기 백기
# https://www.acmicpc.net/problem/15736

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# N개의 깃발을 규칙에 따라 뒤집어 놓았을 때
# 제곱수만 남게 되므로 1~N까지의 제곱수의 개수를 계산
print(int(N**(1/2)))