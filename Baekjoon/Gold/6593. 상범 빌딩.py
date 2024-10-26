# 6593. 상범 빌딩
# https://www.acmicpc.net/problem/6593

import sys, collections
input = sys.stdin.readline

delta = [
    (-1, 0, 0), (1, 0, 0),
    (0, -1, 0), (0, 1, 0),
    (0, 0, -1), (0, 0, 1)
]

# 각 칸에서 인접한 6개의 칸으로 움직여
# 출구를 찾는 것이므로 bfs 구현
def bfs(k, i, j, x):
    qu = collections.deque()
    qu.append((k, i, j, x))

    while qu:
        sk, si, sj, res = qu.popleft()
        
        # 인접한 6개의 칸으로 이동
        for d in delta:
            nk, ni, nj = sk+d[0], si+d[1], sj+d[2]

            # 만약 이동한 곳이 상범 빌딩 안이라면
            # 이동한 곳이 지나갈 수 있는지를 파악
            if 0<=nk<L and 0<=ni<R and 0<=nj<C:

                # 만약 지나갈 수 있는 곳이라면
                # 해당 좌표와 오는 데에 걸린 시간에
                # 1을 더한 값을 qu에 삽입하고
                # 같은 곳을 다시 지나갈 수 없도록
                # 지나갈 수 없는 칸으로 그 값을 갱신
                if building[nk][ni][nj] == '.':
                    qu.append((nk, ni, nj, res+1))
                    building[nk][ni][nj] = '#'

                # 만약 출구라면 오는 데에 걸린 시간 반환
                elif building[nk][ni][nj] == 'E':
                    return res

    # 만약 도중에 함수가 끝나지 않았다면
    # 탈출이 불가능하므로 0 반환
    return 0


# 여러 개의 테스트 케이스로 이루어지므로
# while문으로 계속 입력을 받을 수 있게 함
while True:
    L, R, C = map(int, input().rstrip().split())

    # 만약 L, R, C가 모두 0일 경우
    # 입력이 끝난 것이므로 종료
    if not L and not R and not C:
        break
    
    # 하나의 층을 building에 삽입해 상범 빌딩을 구현
    building = []
    for _ in range(L):
        building.append([list(input().rstrip()) for _ in range(R)])
        input().rstrip()

    # 상범 빌딩에서 시작점을 찾아주고
    # 시작점을 찾았다면 해당 지점에서 출발해
    # 탈출할 수 있는지 bfs 함수를 통해 탐색
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if building[k][i][j] == 'S':
                    x = bfs(k, i, j, 1)

    # 탈출 여부에 따라 적절한 값을 출력
    if x:
        print(f'Escaped in {x} minute(s).')
    else:
        print('Trapped!')