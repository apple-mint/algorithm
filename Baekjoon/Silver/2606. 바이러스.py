# 2606. 바이러스
# https://www.acmicpc.net/problem/2606

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
computers = [[] for _ in range(N+1)]

M = int(input().rstrip())
for _ in range(M):
    com_a, com_b = map(int, input().rstrip().split())

    # 네트워크 상에 서로 연결되어 있다는 표시를 함
    # 양방향으로 연결되어 있으므로 양쪽 컴퓨터에 모두 표시
    computers[com_a].append(com_b)
    computers[com_b].append(com_a)

# 1번 컴퓨터를 시작으로 웜 바이러스에 걸렸는지
# bfs 탐색으로 확인하고자 deque 사용
qu = collections.deque()
visited = [0] * (N+1)

# 1번 컴퓨터를 시작점으로 두고 시작
qu.append(1)
visited[1] = 1

cnt = 0
while qu:
    computer = qu.popleft()

    # 시작점으로부터 연결된 컴퓨터 중 아직 방문하지 않았다면
    # 웜 바이러스에 걸렸지만 아직 표시가 되지 않은 컴퓨터이므로
    # cnt에 1를 더한 뒤 새로운 시작점으로 설정 후 방문표시를 해줌
    for com in computers[computer]:
        if not visited[com]:
            cnt += 1
            qu.append(com)
            visited[com] = 1

# 웜 바이러스에 걸린 컴퓨터의 수를 출력
print(cnt)