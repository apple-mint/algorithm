# 24479. 알고리즘 수업 - 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479

import sys
input = sys.stdin.readline

# BOJ의 채점 서버에서 파이썬의 재귀 최대 깊이는 1,000이므로
# dfs를 재귀로 구현한다면 RecursionError 방지를 위해
# 재귀 최대 깊이를 1,000,000으로 설정해야 함
sys.setrecursionlimit(10**6)

def dfs(start):

    # dfs 함수 바깥에 있는 cnt를
    # 사용하기 위해 global 선언
    global cnt

    # dfs 함수가 호출될 때마다
    # 방문 순서에 1을 더해줌
    cnt += 1

    # 몇번째 방문인지 visited에 표시
    visited[start] = cnt

    # 시작 정점에서 연결되어 있는 정점을 찾아 이동
    # 만약 해당 정점이 아직 방문하지 않는 곳이라면
    # dfs 함수를 호출해 해당 정점으로부터 다시 이동
    for n in graph[start]:
        if not visited[n]:
            dfs(n)


N, M, R = map(int, input().rstrip().split())

# 정점은 1부터 시작하므로 인덱스 번호와
# 맞추기 위해 N+1을 곱해 만들어줌
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 정점은 오름차순으로 방문하므로
# 인접 정점의 요소들을 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 방문 순서를 기록하는 변수 cnt
cnt = 0

# 방문할 수 없는 경우 0으로 출력해야 하므로
# visited 초기값을 다음과 같이 설정
visited = [0]*(N+1)

# 시작 정점 R에서의 모든 노드의
# 방문 순서를 dfs로 확인
dfs(R)

# 출력 예시에 따라 출력
for i in range(1, N+1):
    print(visited[i])