# 17219. 비밀번호 찾기
# https://www.acmicpc.net/problem/17219

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 빠른 탐색을 위해 딕셔너리 사용
memo = {}
for _ in range(N):
    site, password = input().rstrip().split()
    memo[site] = password

# 찾으려는 사이트 주소를 입력받아 비밀번호 출력
for _ in range(M):
    print(memo[input().rstrip()])