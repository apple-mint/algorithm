# 2579. 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

N = int(input().rstrip())

stair = [0] * (N+1)
for i in range(1, N+1):
    stair[i] = int(input().rstrip())

# 게임에서 얻을 수 있는 최댓값인 dp 초기값 설정
dp = [0] * (N+1)
dp[1] = stair[1]

# 만약 N이 1일 경우 stair[2]에서 IndexError가 발생하므로
# 이를 방지하기 위해 N이 1보다 클 경우
# 다음과 같이 dp[2]의 초기값을 만들어줌
if N > 1:
    dp[2] = stair[1] + stair[2]

for i in range(3, N+1):

    # 각 계단마다 게임에서 얻을 수 있는 최댓값을 구해줌
    # 연속해서 세 개의 계단을 밟을 수는 없으므로
    # 다음과 같은 경우의 수가 나옴

    # dp[3] = max(1->3, 2->3)
    # 공통적으로 더해지는 3번째 계단 점수를 제외하고
    # 1, 3끼리 최댓값을 비교

    # dp[4] = max(1->2->4, 1->3->4, 2->4)
    # 2->4는 1->2->4보다 확실히 작으므로 제외,
    # 공통적으로 더해지는 4번째 계단 점수를 제외하고
    # 1->2, 1->3끼리 최댓값을 비교

    # dp[5] = max(1->2->4->5, 1->3->5, 2->3->5, 2->4->5)
    # 2->4->5는 1->2->4->5보다 확실히 작으므로 제외,
    # 공통적으로 더해지는 5번째 계단 점수를 제외하고
    # 1->2->4, 1->3, 2->3끼리 최댓값을 비교

    # 1->3, 2->3 중 최댓값이 P[3]이고 둘 모두
    # 연속해서 세 개의 계단을 밟은 것이 아니므로 P[3]으로 비교

    # 1->2->4는 P[4]가 1->3->4일 가능성이 있으므로
    # 그 이전 값인 1->2 중 최댓값인 P[2]에
    # 4번째 칸의 점수를 더해준 것으로 비교

    # 따라서 다음과 같은 점화식을 쓸 수 있음
    # 비교한 두 값의 최댓값에 현재 계단 점수를 더해 dp에 삽입
    dp[i] = max(dp[i-2], dp[i-3]+stair[i-1]) + stair[i]

print(dp[N])