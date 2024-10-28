# 1182. 부분수열의 합
# https://www.acmicpc.net/problem/1182

import sys, itertools
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

# 부분수열이라 함은 N개의 정수를
# 1개부터 N개까지 선택하는 모든 경우의 수이고
# 그 경우의 수 중 선택한 원소들의 합이 S가 되어야 하므로
# 조합을 통해 모든 경우의 수를 구해 해당되는 경우의 수를 찾음
cnt = 0
for i in range(1, N+1):
    combis = itertools.combinations(nums, i)

    # 선택한 원소들의 합이 S일 경우
    # cnt에 1을 더해줌
    for combi in combis:
        if sum(combi) == S:
            cnt += 1

# 합이 S가 되는 부분수열의 개수 출력
print(cnt)