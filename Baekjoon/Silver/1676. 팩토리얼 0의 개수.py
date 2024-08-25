# 1676. 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 0의 개수는 2와 5의 쌍 개수이므로
# 1~N까지의 수를 곱할 때 해당 쌍이 몇 개 나오는지 계산
# 5의 배수가 2의 배수보다 그 수가 적으므로
# 1~N까지 해당 수에 5가 몇 번 곱해지는지만 계산
cnt = 0
for n in range(1, N+1):
    while not n%5:
        n //= 5
        cnt += 1

print(cnt)