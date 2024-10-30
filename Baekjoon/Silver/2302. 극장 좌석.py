# 2302. 극장 좌석
# https://www.acmicpc.net/problem/2302

import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

vips = []
for _ in range(M):
    vip = int(input().rstrip())
    vips.append(vip)

# 입장권 번호를 기준으로 좌우로 자리를 옮겨
# 좌석에 앉는 경우의 수를 dp를 통해 구함
dp = [1, 1, 2]
for n in range(2, N):
    dp.append(dp[n]+dp[n-1])

ans = 1

# 만약 vip가 없는 경우 모든 사람들이
# 좌우로 자리를 옮겨 앉을 수 있으므로
# 구한 값 그대로 ans에 갱신
if not M:
    ans = dp[N]

# 만약 vip가 있는 경우 vip를 제외한 사람들끼리
# 좌우로 자리를 옮겨 앉을 수 있으므로
# 해당 구간끼리 좌석에 앉는 경우의 수를 구해 곱해줌
else:
    pre = 0
    for i in range(M):
        ans *= dp[vips[i]-pre-1]
        pre = vips[i]
    ans *= dp[N-pre]

print(ans)