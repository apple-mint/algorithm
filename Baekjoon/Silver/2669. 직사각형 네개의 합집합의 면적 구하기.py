# 2669. 직사각형 네개의 합집합의 면적 구하기
# https://www.acmicpc.net/problem/2669

import sys
input = sys.stdin.readline

# 직사각형을 놓을 평면 설정
# 1~100 범위의 x, y좌표를 포함할 수 있도록 범위를 101로 설정
plane = [[0] * 101 for _ in range(101)]
cnt = 0

for _ in range(4):
    lx, ly, rx, ry = map(int, input().rstrip().split())

    # 제시된 점을 기준으로 칸 당 직사각형이 놓여 있는지를 확인
    # 이전에 직사각형이 없었던 평면이라면
    # 그 칸에 직사각형이 놓였다는 뜻으로 1로 바꿔주고 cnt에 1를 더함
    for x in range(lx, rx):
        for y in range(ly, ry):
            if not plane[x][y]:
                cnt += 1
                plane[x][y] = 1

# 직사각형이 놓여 있는 칸 수,
# 즉 직사각형이 차지하는 면적 출력
print(cnt)