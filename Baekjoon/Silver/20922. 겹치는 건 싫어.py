# 20922. 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922

import sys, collections
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

nums = collections.defaultdict(int)

start = 0
end = 0
ans = 0

# 길이가 N인 수열의 요소를 하나하나 탐색
while end < N:

    # 만약 해당 정수가 연속 부분 수열 내에서 K개 미만일 때
    # 연속 부분 수열의 마지막으로 추가할 수 있으므로
    # 해당 정수의 개수와 끝 인덱스에 1을 더해줌
    # 이전보다 길이가 길어졌으므로
    # 해당 값이 최장값인지 확인하고 그렇다면 값을 갱신
    if nums[arr[end]] < K:
        nums[arr[end]] += 1
        end += 1
        ans = max(ans, end-start)
    
    # 만약 K개 이상이라면 마지막으로 추가할 수 없으므로
    # 연속 부분 수열을 유지하기 위해 맨 앞에 있는 정수를 제거
    # 해당 정수의 개수에 1을 빼주고 시작 인덱스에 1을 더해줌
    else:
        nums[arr[start]] -= 1
        start += 1

# 구한 최장 연속 부분 수열의 길이 출력
print(ans)