# 11727. 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 오른쪽 끝이 2x1 타일 2개일 경우
# 2x1 타일 2개, 2x2 타일 1개로도 채울 수 있어
# 이전보다 방법의 수가 2배 늘어난다는 사실을 고려하며
# 2xn 크기의 직사각형을 채우는 방법의 수를
# 하나하나 계산했을 때 그 결과는 아래와 같음

# n = 1 -> 1
# n = 2 -> 1 + 2*1 = 3
# n = 3 -> 3 + 2*1 = 5
# n = 4 -> 5 + 2*3 = 11
# n = 5 -> 11 + 2*5 = 21
# n = 6 -> 21 * 2*11 = 43

# 위의 결과에서 찾은 규칙성을 바탕으로 도출한
# dp[n] = dp[n-1] + 2*dp[n-2] 점화식을 활용해
# 2xn 크기의 직사각형을 채우는 방법의 수를 계산

dp = [0, 1, 3]

for num in range(2, n):
    dp.append(dp[num] + 2*dp[num-1])

print(dp[n]%10007)