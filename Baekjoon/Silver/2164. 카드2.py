# 2164. 카드2
# https://www.acmicpc.net/problem/2164

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

# 제일 위에 있는 카드를 버리는 동작을
# popleft 메서드로 빠르게 구현하기 위해 deque 사용
qu = collections.deque()

# 주어진 정수 1부터 N까지의 번호가 붙어 있는
# 카드는 순서대로 놓음
for card in range(1, N+1):
    qu.append(card)

# 마지막에 카드가 하나 남을 때까지
# 제일 위에 있는 카드를 버리고
# 그 다음 카드를 제일 아래로 옮기는 동작을 반복
while len(qu) > 1:
    qu.popleft()
    qu.append(qu.popleft())

# 마지막에 남게 되는 카드 번호 출력
print(*qu)