# 18352. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys, collections
input = sys.stdin.readline

# bfs 탐색을 통해 거리를 구함
def bfs():
    qu = collections.deque()
    visited = [-1] * (N+1)
    
    # 출발도시인 X를 삽입하고
    # X->X까지는 항상 0이므로 0으로 방문표시
    qu.append(X)
    visited[X] = 0

    while qu:
        start = qu.popleft()

        # 만약 도시와 연결되어 있는 이동할 도시가
        # 방문하지 않은 곳이라면 qu에 삽입하고
        # 이전거리 + 1을 하여 거리를 기록
        for move in cities[start]:
            if visited[move] == -1:
                qu.append(move)
                visited[move] = visited[start] + 1

    # X에서 모든 도시를 다 돌았다면
    # 거리가 기록된 리스트를 반환
    return visited


N, M, K, X = map(int, input().rstrip().split())
cities = [[] for _ in range(N+1)]

# 단방향 도로이므로 A->B 한 방향만 연결
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    cities[A].append(B)

# 도시 X에서 출발해 도달할 수 있는 모든 도시의 거리를
# bfs 탐색을 통해 구하고 그 값을 담은 리스트 반환
distance = bfs()

ans = []

# 모든 도시를 탐색하면서
# 기록된 거리가 K와 같다면 ans에 삽입
for city in range(1, N+1):
    if distance[city] == K:
        ans.append(city)

# 출력형태에 따라 출력
# 1부터 N까지의 도시를 순차적으로 탐색했으므로
# 별도로 오름차순 정렬을 하지 않아도 됨
if ans:
    print(*ans, sep='\n')
else:
    print(-1)