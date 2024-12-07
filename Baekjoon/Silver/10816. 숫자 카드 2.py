# 10816. 숫자 카드 2
# https://www.acmicpc.net/problem/10816

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
cards = list(map(int, input().rstrip().split()))

# 상근이가 해당 숫자 카드를 몇 개 가지고 있는지
# 빠르게 탐색하기 위해 defaultdict 사용해
# 가지고 있는 숫자 카드의 수를 기록
cnt = collections.defaultdict(int)
for card in cards:
    cnt[card] += 1

M = int(input().rstrip())
check = list(map(int, input().rstrip().split()))

# 상근이가 해당 숫자 카드를 몇 개 가지고 있는지
# 주어진 M개의 순서대로 그 수를 answers에 삽입
answers = []
for c in check:
    answers.append(cnt[c])

# 출력 예시에 따라 출력
print(*answers)