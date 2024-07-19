# 11724. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys, collections
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 해당되는 정점번호에 어떤 정점이 연결되어있는지 기록
# 정점번호는 1부터 시작되므로 인덱스 번호를 맞추기 위해 N에 1을 더함
components = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    
    # 방향 없는 그래프이므로 양쪽에 모두 표시
    components[u].append(v)
    components[v].append(u)

# BFS 탐색 위해 deque 사용
qu = collections.deque()

# 방문을 했는지를 표시
visited = [0] * (N+1)

# 연결 요소의 개수를 기록한 변수 선언 후 탐색
cnt = 0
for num in range(1, N+1):

    # 한 정점이 다른 정점과 이어져 있지 않더라도
    # 연결 요소이므로 처음 탐색한 정점이면
    # 1을 더해주고 방문표시
    if not visited[num]:
        cnt += 1
        visited[num] = 1

        # 만약 해당 정점과 이어진 정점이 있다면
        # BFS 탐색을 통해 연결값을 탐색
        if components[num]:
            qu.append(num)

        while qu:
            start = qu.popleft()

            for compo in components[start]:
                if not visited[compo]:
                    qu.append(compo)
                    visited[compo] = 1

print(cnt)