# 24481. 알고리즘 수업 - 깊이 우선 탐색 3
# https://www.acmicpc.net/problem/24481

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 깊이 우선 탐색으로 시작 정점에서부터
# 모든 노드의 깊이를 탐색하는 함수
def dfs(R, depth):

    # 방문 정점에 시작 정점으로부터
    # 깊이가 몇인지를 표시
    visited[R] = depth
    
    # 방문 정점과 인접한 정점들 중
    # 방문하지 않은 정점이 있는지 탐색
    for x in graph[R]:

        # 만약 방문하지 않은 정점이 있다면
        # 해당 정점으로부터 깊이를 탐색하기 위해
        # 방문하지 않은 정점과 깊이에 1을 더한 값을
        # dfs 함수에 전달하며 호출
        if visited[x] == -1:
            dfs(x, depth+1)


N, M, R = map(int, input().rstrip().split())

# 정점의 수가 1부터 시작하므로
# 인덱스 번호를 맞추기 위해 N+1로 만듦
graph = [[] for _ in range(N+1)]

# 간선의 수만큼 정점들을 연결
# 양방향 간선이므로 양쪽을 모두 연결
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순으로 방문하기 위해
# 각 정점마다 연결된 정점들을 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 모든 노드의 깊이를 담을 리스트
# 방문되지 않은 노드의 깊이는 -1로 하므로
# 해당값을 초기값으로 설정
visited = [-1] * (N+1)

# 시작 정점에서부터 dfs 시작
dfs(R, 0)

# 출력 양식에 따라 출력
print(*visited[1:], sep='\n')