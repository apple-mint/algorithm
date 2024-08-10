# 26069. 붙임성 좋은 총총이
# https://www.acmicpc.net/problem/26069

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 처음 무지개 댄스를 추고 있는 사람은 총총이 뿐이므로
# 이름과 춤을 추고 있다는 상태라는 의미의 1을 딕셔너리에 추가
dance = {'ChongChong': 1}

for _ in range(N):
    A, B = input().rstrip().split()

    # 사람들이 만난 기록이 주어졌을 때
    # 둘 중 한 명이 무지개 댄스를 추고 있다면,
    # 즉 dance에 값이 존재한다면 둘 다 춤을 주는 상태로 값 갱신
    if dance.get(A) or dance.get(B):
        dance[A] = 1
        dance[B] = 1

# 춤을 추고 있는 상태의 사람이 몇 명인지
# 그 수를 더해 출력
print(sum(dance.values()))