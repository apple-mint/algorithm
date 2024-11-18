# 11403. 경로 찾기
# https://www.acmicpc.net/problem/11403

import sys, collections
input = sys.stdin.readline

# 정점 i를 시작으로 갈 수 있는 모든 정점을 방문함으로써
# 양수인 경로가 있는지 탐색하고자 bfs 구현
def bfs(start):
    qu = collections.deque()
    visited = [0]*N

    # 시작점을 qu에 삽입해
    # bfs를 위한 초기값 설정
    qu.append(start)

    # bfs 시작
    while qu:
        move = qu.popleft()

        for j in range(N):

            # 가중치 없는 방향 그래프 G를 확인해
            # 해당 정점에서 아직 방문하지 않은 정점이면서
            # 간선이 존재해 갈 수 있는 정점이 있는지 확인
            if G[move][j] and not visited[j]:

                # 만약 있다면 qu에 해당 정점을 삽입하고
                # 방문표시를 해 중복 탐색을 방지
                qu.append(j)
                visited[j] = 1

                # 시작점에 해당하는 줄의 j번째 숫자를
                # 1로 바꿔 양수인 경로가 있음을 표시
                answer[start][j] = 1

    return


N = int(input().rstrip())
G = [list(map(int, input().rstrip().split())) for _ in range(N)]

answer = [[0]*N for _ in range(N)]

# 모든 정점을 시작점으로 삼아
# 정점 i에서 j로 가는 길이가
# 양수인 경로가 있는지 확인
for i in range(N):
    bfs(i)

# 출력 예시에 따라 출력
for i in range(N):
    print(*answer[i])