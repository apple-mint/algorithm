# 9461. 파도반 수열
# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

# P[N] = P[N-2] + P[N-3] 규칙을 가지는 파도반 수열
P = {
    1:1, 2:1, 3:1, 4:2, 5:2,
    6:3, 7:4, 8:5, 9:7, 10:9
}

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())

    # 만약 N이 10 이하라면 이미 값이 있으므로
    # 따로 계산할 필요 없이 해당되는 값을 출력
    if N <= 10:
        print(P[N])

    else:
        # 만약 N에 해당하는 파도반 수열이 없다면
        # 마지막 파도반 수열 다음부터
        # 주어진 N까지 규칙에 따라 계산
        if not P.get(N):
            n = len(P)+1

            while n <= N:
                P[n] = P[n-2] + P[n-3]
                n += 1
        
        # 만들어진 파도반 수열 출력
        print(P[N])