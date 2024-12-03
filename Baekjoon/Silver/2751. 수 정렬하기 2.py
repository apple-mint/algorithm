# 2751. 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 리스트 컴프리헨션 문법을 통해
# N개의 수를 입력받음
nums = [int(input().rstrip()) for _ in range(N)]

# 오름차순으로 정렬
nums.sort()

# 출력 예시에 따라 한 줄에 하나씩 출력
print(*nums, sep='\n')