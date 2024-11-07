# 13549. 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

import sys, collections
input = sys.stdin.readline

# 해당 위치에서 이동할 수 있는 방법들로
# 다른 위치로 이동했을 때 목적지인지를
# 빠르게 확인하기 위해 bfs 구현
def bfs(start):

    qu = collections.deque()
    visited = [-1] * 100001

    qu.append(start)
    visited[start] = 0

    # bfs 시작
    while qu:
        X = qu.popleft()

        # 만약 수빈이가 있는 위치가
        # 동생이 있는 위치라면
        # 여태까지 이동하는 데에 걸린 시간을 반환
        if X == K:
            return visited[K]

        # 해당 위치에서 순간이동을 했을 때
        # 순간이동을 한 곳이 점 범위 내고
        # 방문하지 않았던 곳이라면
        # qu에 이동한 위치 좌표를 삽입하고
        # 이동하는 데에 걸린 시간을 갱신

        # 순간이동은 별도로 시간이 걸리지 않으므로
        # 이전에 이동하는 데에 걸린 시간을 그대로 갱신
        if 0<=2*X<=100000 and visited[2*X] == -1:
            qu.append(2*X)
            visited[2*X] = visited[X]

        # 해당 위치에서 이동할 수 있는 방법으로 이동했을 때
        # 이동한 곳이 범 범위 내고 방문하지 않았던 곳이라면
        # qu에 이동한 위치 좌표를 삽입하고
        # 이전에 이동하는 데에 걸린 시간에 1을 더한 값을
        # 이동하는 데에 걸린 시간으로 갱신
        for move in (X-1, X+1):
            if 0<=move<=100000 and visited[move] == -1:
                qu.append(move)
                visited[move] = visited[X] + 1


N, K = map(int, input().rstrip().split())

# bfs 함수를 호출해 동생을 찾는
# 가장 빠른 시간을 구하고 이를 출력
print(bfs(N))