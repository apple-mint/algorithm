# 14425. 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 빠른 탐색을 위해 in 연산속도가 빠른 set 사용
S = set()
for _ in range(N):
    S.add(input().rstrip())

cnt = 0
for _ in range(M):
    word = input().rstrip()

    # 검사해야 하는 문자열이
    # 집합 S에 있는지 확인 후
    # 있다면 cnt에 1을 더해줌
    if word in S:
        cnt += 1

# M개의 문자열 중 총 몇 개가
# 집합 S에 포함되어 있는지 출력
print(cnt)