# 7568. 덩치
# https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

N = int(input().rstrip())

people = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    people.append((x, y))

# 각 사람의 덩치 등수는 자신보다 더 큰
# 덩치의 사람의 수에서 1을 더한 값이므로
# 자신보다 덩치가 큰 사람이 몇 명인지를 구함
ans = []
for p1 in people:
    k = 1
    for p2 in people:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            k += 1
    
    # 구한 덩치 등수를 삽입
    ans.append(k)

print(*ans, sep=' ')