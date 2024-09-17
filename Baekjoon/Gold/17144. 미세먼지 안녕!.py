# 17144. 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

import sys, copy
input = sys.stdin.readline

# 상하좌우 좌표값
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 미세먼지 확산
def spread():

    # 모든 칸에서 동시에 일어나므로
    # 확산된 미세먼지 양을 기록할 별도의 방 복사
    res = copy.deepcopy(room)

    for r in range(R):
        for c in range(C):

            # 만약 해당 칸에 미세먼지가 있다면
            # 해당 미세먼지 양을 5로 나눈 몫이 확산되므로
            # 확산되는 미세먼지 양을 계산
            if room[r][c] > 0:
                dust = room[r][c] // 5
                cnt = 0

                # 인접한 네 방향으로 이동
                for de in delta:
                    nr = r + de[0]
                    nc = c + de[1]
                    
                    # 인접한 칸이 방 내에 있고
                    # 해당 칸에 공기청정기가 없다면
                    # 별도로 복사한 방에 미세먼지 확산을 기록
                    if 0<=nr<R and 0<=nc<C and room[nr][nc] != -1:
                        cnt += 1
                        res[nr][nc] += dust
                
                # 기존 미세먼지 양에서
                # 미세먼지가 확산된 양만큼 빼고
                # 해당 값을 별도로 복사한 방에 기록
                res[r][c] -= dust * cnt

    return res


# 공기청정기 작동
def clean():

    # 현재 미세먼지 양을 순환방향대로 움직여서 온
    # 미세먼지 양으로 바꾸며 공기청정기 위쪽 작동 구현

    # 위에서 아래로 이동
    for a in range(up-1, 0, -1):
        room[a][0] = room[a-1][0]

    # 오른쪽에서 왼쪽으로 이동
    for b in range(C-1):
        room[0][b] = room[0][b+1]

    # 아래에서 위로 이동
    for c in range(up):
        room[c][C-1] = room[c+1][C-1]

    # 왼쪽에서 오른쪽으로 이동
    for d in range(C-1, 1, -1):
        room[up][d] = room[up][d-1]
    
    # 공기청정기 위쪽 바로 오른쪽에 있는 칸은
    # 미세먼지가 없어지므로 0으로 값 갱신
    room[up][1] = 0
    
    # 현재 미세먼지 양을 순환방향대로 움직여서 온
    # 미세먼지 양으로 바꾸며 공기청정기 아래쪽 작동 구현
    
    # 아래에서 위로 이동
    for e in range(down+1, R-1):
        room[e][0] = room[e+1][0]

    # 오른쪽에서 왼쪽으로 이동
    for f in range(C-1):
        room[R-1][f] = room[R-1][f+1]

    # 위에서 아래로 이동
    for g in range(R-1, down, -1):
        room[g][C-1] = room[g-1][C-1]

    # 왼쪽에서 오른쪽으로 이동
    for h in range(C-1, 1, -1):
        room[down][h] = room[down][h-1]

    # 공기청정기 아래쪽 바로 오른쪽에 있는 칸은
    # 미세먼지가 없어지므로 0으로 값 갱신
    room[down][1] = 0

    return


R, C, T = map(int, input().rstrip().split())
room = [list(map(int, input().rstrip().split())) for _ in range(R)]

# 공기청정기가 설치된 곳 확인
up, down = 0, 0
for r in range(R):
    if room[r][0] == -1:
        up = r
        down = r+1
        break

# T초 동안 미세먼지 확산 및 공기청정기 작동
for _ in range(T):
    room = spread()
    clean()

# 공기청정기가 설치된 곳을 -1로 표시했으므로
# 해당 칸의 값이 자연수일 때만 더해
# 남아있는 미세먼지 양을 계산
ans = 0
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            ans += room[r][c]

print(ans)