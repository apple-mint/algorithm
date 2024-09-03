# 1697. 숨바꼭질
# https://www.acmicpc.net/problem/1697

import sys, collections
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

# 가장 빠른 시간이 몇 초 후인지 알기 위해 bfs 사용
qu = collections.deque()
location = [-1] * 100001

# 수빈이가 있는 위치를 qu에 삽입하고
# 해당 시간을 0초로 설정
qu.append(N)
location[N] = 0

# bfs 시작
while qu:

    # 수빈이가 있는 현재 위치
    X = qu.popleft()

    # 만약 수빈이가 동생이 있는 위치까지 왔다면
    # 해당 초를 출력하고 탐색 종료
    if X == K:
        print(location[X])
        break

    # 수빈이가 이동할 수 있는 경우로 이동했을 때
    # 이동할 수 있는 범위 내에 있고 방문하지 않은 경우
    # 이동한 위치에서 다시 이동하기 위해
    # qu에 이동한 위치를 삽입하고 걸린 시간으로 값 갱신
    for move in (X-1, X+1, 2*X):
        if 0<=move<100001 and location[move] == -1:
            qu.append(move)
            location[move] = location[X] + 1