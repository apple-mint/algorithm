# 1439. 뒤집기
# https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline

S = input().rstrip()

idx = 0
zero = 0
one = 0

# S의 모든 철자를 하나씩 비교하며
# 연속된 하나 이상의 1, 0을 찾음
while idx < len(S):

    # 만약 연속된 하나 이상의
    # 0이 있는 경우 zero에 1을 더해줌
    if S[idx] == '0':
        while idx+1 < len(S) and S[idx] == S[idx+1]:
            idx += 1
        zero += 1

    # 만약 연속된 하나 이상의
    # 1이 있는 경우 one에 1을 더해줌
    else:
        while idx+1 < len(S) and S[idx] == S[idx+1]:
            idx += 1
        one += 1

    # 다음 철자가 무엇인지 확인하기 위해
    # idx에 1을 더해 다음 철자로 이동
    idx += 1

# 0, 1 중 더 적게 나온 값을 바꾸는 것이
# 행동을 최소로 하는 것이므로 둘의 최솟값을 출력 
print(min(zero, one))