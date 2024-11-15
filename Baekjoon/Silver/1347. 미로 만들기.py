# 1347. 미로 만들기
# https://www.acmicpc.net/problem/1347

import sys
input = sys.stdin.readline

delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]

N = int(input().rstrip())
words = input().rstrip()

# 홍준이 있는 미로 안의 한 칸이 고정되어 있지 않으므로
# 홍준이가 이동할 수 있는 최대한의 범위만큼 설정
area = [[0]*100 for _ in range(100)]

# 홍준이 있는 미로 안의 한 칸과
# 바라보고 있는 방향 초기값 설정
i, j = 49, 49
direction = 0

# 홍준이 있는 미로 안의 한 칸은
# 이동할 수 있는 칸이므로 1로 표시
area[i][j] = 1

# 홍준이가 적은 내용에 따라 이동
for word in words:

    # 만약 'F'일 경우 앞으로 한 칸 움직이고
    # 이동한 칸에 이동할 수 있는 칸임을 1로 표시
    if word == 'F':
        i += delta[direction][0]
        j += delta[direction][1]
        area[i][j] = 1

    # 만약 'L'일 경우 방향을 왼쪽으로 전환
    elif word == 'L':
        direction = (direction-1) % 4
    
    # 만약 'R'일 경우 방향을 오른쪽으로 전환
    elif word == 'R':
        direction = (direction+1) % 4

# 미로의 시작과 끝 좌표 초기값 설정
si, sj = 100, 100
ei, ej = 0, 0

# 이동할 수 있는 칸의 좌표를 확인하며
# 미로의 시작과 끝 좌표를 구함
for i in range(100):
    for j in range(100):
        if area[i][j]:
            si, sj = min(si, i), min(sj, j)
            ei, ej = max(ei, i), max(ej, j)

# 이동할 수 있는 칸은 '.',
# 벽은 '#'으로 표시하며 미로 지도 출력
for i in range(si, ei+1):
    ans = []
    for j in range(sj, ej+1):
        if area[i][j]:
            ans.append('.')
        else:
            ans.append('#')
    
    print(*ans, sep='')