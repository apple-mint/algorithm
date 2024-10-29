# 10157. 자리배정
# https://www.acmicpc.net/problem/10157

import sys
input = sys.stdin.readline

C, R = map(int, input().rstrip().split())
K = int(input().rstrip())

# 공연장에 있는 좌석의 수보다
# 대기번호의 수가 크다면
# 배정할 좌석이 없으므로 0 출력
if K > C*R:
    print(0)

else:
    seat = [[0]*C for _ in range(R)]

    # 대기번호 1인 사람을
    # 처음 시작위치에 해당하는 좌석에 배정하고
    # 사람이 앉아 있다는 표시를 해줌
    si, sj = 0, 0
    cnt = 1
    seat[si][sj] = cnt

    # 대기 순서가 K인 사람이 앉을 때까지
    # 좌석을 배정하는 순서에 따라 배정
    while cnt < K:

        # 위쪽으로 가면서 배정
        while si+1 < R and not seat[si+1][sj] and cnt < K:
            si += 1
            cnt += 1
            seat[si][sj] = cnt

        # 오른쪽으로 가면서 배정
        while sj+1 < C and not seat[si][sj+1] and cnt < K:
            sj += 1
            cnt += 1
            seat[si][sj] = cnt

        # 아래쪽으로 가면서 배정
        while si-1 > -1 and not seat[si-1][sj] and cnt < K:
            si -= 1
            cnt += 1
            seat[si][sj] = cnt

        # 왼쪽으로 가면서 배정
        while sj-1 > -1 and not seat[si][sj-1] and cnt < K:
            sj -= 1
            cnt += 1
            seat[si][sj] = cnt

    # i, j이 0 ~ N-1까지 인덱스가 있으므로
    # 1, 1부터 시작하는 x, y에 맞춰 1씩 더하고
    # x, y 방향에 맞게 적절한 값을 정해주고 출력
    x, y = sj+1, si+1
    print(x, y)