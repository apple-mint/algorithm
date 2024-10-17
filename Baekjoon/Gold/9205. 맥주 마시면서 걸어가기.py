# 9205. 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

import sys, collections
input = sys.stdin.readline

# 갈 수 있는 이동 범위 내에서
# 편의점 또는 펜타포트 락 페스티벌에
# 도착할 수 있는지를 확인하고자 bfs 구현
def bfs(x, y):

    qu = collections.deque()
    visited = [0]*n

    qu.append((x, y))

    # bfs 시작
    while qu:
        sx, sy = qu.popleft()

        # 50미터를 이동할 때마다 맥주를 한 병씩 마시고
        # 맥주는 한 박스에 20개 들어 있으므로
        # 갈 수 있는 최대 거리는 1,000미터가 됨
        # 이를 고려해 목적지에 도착할 수 있을지를 판단

        # 만약 현재 위치에서 페스티벌에
        # 도착할 수 있다면 'happy' 반환
        if abs(sx-fx)+abs(sy-fy) <= 1000:
            return 'happy'
        
        # 아니라면 이동거리를 초기화하기 위해
        # 편의점에 갈 수 있는지 모든 편의점을 탐색
        for i in range(n):

            # 만약 아직 가지 않은 편의점이라면
            # 두 좌표 사이의 거리를 구하기 위해
            # 해당 편의점의 x, y좌표를 변수에 저장
            if not visited[i]:
                nx, ny = store[i]

                # 만약 해당 편의점에 갈 수 있다면
                # 해당 편의점을 새로운 시작점으로 삼고자
                # qu에 좌표를 삽입하고 방문표시를 함
                if abs(sx-nx)+abs(sy-ny) <= 1000:
                    qu.append((nx, ny))
                    visited[i] = 1
    
    # 도중에 종료되지 않았다면 맥주가 바닥나
    # 더 이동할 수 없는 상태이므로 'sad' 반환
    return 'sad'


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    # 상근이네 집 좌표
    hx, hy = map(int, input().rstrip().split())

    # 편의점 좌표
    store = []
    for _ in range(n):
        x, y = map(int, input().rstrip().split())
        store.append((x, y))

    # 펜타포트 락 페스티벌 좌표
    fx, fy = map(int, input().rstrip().split())
    
    # 페스티벌에 도착할 수 있는지 없는지
    # bfs 함수를 통해 확인하고
    # 이에 대한 결과를 출력
    print(bfs(hx, hy))