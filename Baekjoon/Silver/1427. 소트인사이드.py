# 1427. 소트인사이드
# https://www.acmicpc.net/problem/1427

import sys
input = sys.stdin.readline

nums = list(map(int, input().rstrip()))

# 자리수를 내림차순으로 정렬
nums.sort(reverse=True)

# 정렬한 수를 출력
print(*nums, sep='')