# 16173. 점프왕 쩰리 (Small)
# https://www.acmicpc.net/problem/16173

import sys, collections
input = sys.stdin.readline

# 기준점에서 오른쪽, 아래쪽으로
# 이동할 수 있는 곳으로 이동한 뒤
# 해당 지점에서 위와 같은 연산을 반복하므로
# 인접한 곳을 탐색하는 bfs 구현
def bfs():
    qu = collections.deque()
    visited = [[0]*N for _ in range(N)]
    
    # 출발점이 정사각형의 가장 왼쪽,
    # 가장 위의 칸이므로 이에 맞게 초기값 설정
    qu.append((0, 0))
    visited[0][0] = 1

    # bfs 시작
    while qu:
        si, sj = qu.popleft()

        # 현재 밟고 있는 칸에 있는 수이자
        # 쩰리가 한번에 이동할 수 있는 칸의 수
        num = area[si][sj]

        # 만약 현재 밟고 있는 칸의 수가 -1일 경우
        # 게임판의 승리 지점에 도달한 것이므로 HaruHaru 반환
        if num == -1:
            return 'HaruHaru'

        # 이동할 수 있는 만큼 오른쪽으로 이동했을 때
        # 이동한 곳이 게임 구역 범위 내에 있고
        # 아직 방문하지 않은 곳이라면
        # 해당 지점에서 이동할 수 있는지 확인하고자
        # qu에 해당 좌표를 삽입하고 방문표시를 함
        if 0<=sj+num<N and not visited[si][sj+num]:
            qu.append((si, sj+num))
            visited[si][sj+num] = 1

        # 이동할 수 있는 만큼 아래로 이동했을 때
        # 이동한 곳이 게임 구역 범위 내에 있고
        # 아직 방문하지 않은 곳이라면
        # 해당 지점에서 이동할 수 있는지 확인하고자
        # qu에 해당 좌표를 삽입하고 방문표시를 함
        if 0<=si+num<N and not visited[si+num][sj]:
            qu.append((si+num, sj))
            visited[si+num][sj] = 1

    # qu에 좌표가 없어질 때까지
    # 승리 지점에 도달하지 못했다면 Hing 반환
    return 'Hing'


N = int(input().rstrip())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

# bfs 함수에 따른 결과값 출력
print(bfs())