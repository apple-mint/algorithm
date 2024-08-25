# 1260. DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys, collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):

    # dfs 함수가 호출될 때마다
    # 시작 정점에 방문표시를 해주고
    # 방문점을 순서대로 출력하고자
    # 해당 사항을 기록하는 리스트에 정점 번호 삽입
    dfs_visited[start] = 1
    dfs_ans.append(start)

    # 시작 정점과 연결된 점들을 순차적으로 탐색했을 경우
    # 만약 해당 정점을 방문하지 않았다면 dfs 함수 호출
    for move in graph[start]:
        if not dfs_visited[move]:
            dfs(move)

    return


def bfs(start):
    qu = collections.deque()

    # qu에 시작 정점을 삽입하고 방문표시를 해주고
    # 방문점을 순서대로 출력하고자
    # 해당 사항을 기록하는 리스트에 정점 번호 삽입
    qu.append(start)
    bfs_visited[start] = 1
    bfs_ans.append(start)

    while qu:

        # qu에 첫번째 요소를 가져와
        # 해당 정점을 시작 정점으로 삼음
        start = qu.popleft()

        # 시작 정점과 연결된 점들을 순차적으로 탐색했을 경우
        # 만약 해당 정점을 방문하지 않았다면
        # 해당 정점을 이후의 시작 정점으로 삼기 위해
        # qu에 해당 정점 삽입, 방문표시를 해주고
        # 방문순서를 기록하는 리스트에 해당 정점 번호 삽입
        for move in graph[start]:
            if not bfs_visited[move]:
                qu.append(move)
                bfs_visited[move] = 1
                bfs_ans.append(move)

    return


N, M, V = map(int, input().rstrip().split())

# 간선으로 연결된 두 정점 표시
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 정점이 여러 개인 경우
# 정점 번호가 작은 것부터 방문하므로
# 연결된 정점 목록을 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 시작 정점 V에서 dfs, bfs
dfs_visited, bfs_visited = [0]*(N+1), [0]*(N+1)
dfs_ans, bfs_ans = [], []
dfs(V), bfs(V)

# 출력 예시에 따라 출력
print(*dfs_ans, sep=' ')
print(*bfs_ans, sep=' ')