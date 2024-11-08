# 12851. 숨바꼭질 2
# https://www.acmicpc.net/problem/12851

import sys, collections
input = sys.stdin.readline

# 수빈이가 가장 빠른 시간 내에
# 동생을 찾는 경우를 찾기 위해 bfs 구현
def bfs(start):

    qu = collections.deque()
    visited = [-1] * 100001
    cnt = 0

    # 초기값 설정
    qu.append(start)
    visited[start] = 0

    # bfs 시작
    while qu:
        X = qu.popleft()

        # 만약 수빈이가 동생을 찾았을 경우
        # cnt에 1을 더하고 아래의 식 무시
        if X == K:
            cnt += 1
            continue

        # 수빈이가 이동한 경우의 수대로 이동했을 때
        # 이동한 곳이 범위 내에 있는지 확인
        for move in (X-1, X+1, 2*X):
            if 0<=move<=100000:

                # 이동한 곳이 전에 방문하지 않았던 곳이거나
                # 전에 방문했던 것보다 더 빠른 시간 내에 방문한 경우
                # qu에 해당 위치를 삽입하고
                # 이전에 방문하는 데에 걸린 시간에 1을 더해 갱신
                if visited[move] == -1 or visited[move] > visited[X]:
                    qu.append(move)
                    visited[move] = visited[X] + 1
    
    # 수빈이가 동생을 찾는 가장 빠른 시간,
    # 가장 빠른 시간으로 동생을 찾는 방법의 수 반환
    return visited[K], cnt


N, K = map(int, input().rstrip().split())

# 출력 예시에 따라 각각 반환값을 출력
print(*bfs(N), sep='\n')