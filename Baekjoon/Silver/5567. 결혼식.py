# 5567. 결혼식
# https://www.acmicpc.net/problem/5567

import sys, collections
input = sys.stdin.readline

# 상근이의 친구와 친구의 친구가 누구인지
# 확인하기 위해 bfs 구현
def bfs():

    qu = collections.deque()
    visited = [0]*(n+1)

    # 상근이의 학번인 1을 넣어
    # bfs를 위한 초기값 설정
    qu.append(1)

    # bfs 시작
    while qu:
        people = qu.popleft()

        # 만약 선택한 사람과 친구인 사람들 중
        # 아직 친구 관계가 파악되지 않은 사람이 있다면
        # qu에 해당 학번을 삽입하고
        # 상근이로부터 거리가 얼마만큼 떨어져있는지 확인하고자
        # 이전 값에 1을 더한 값을 visited에 표시
        for friend in friends[people]:
            if not visited[friend]:
                qu.append(friend)
                visited[friend] = visited[people] + 1

    cnt = 0

    # 상근이를 제외한 학교 동기 중
    # 친구, 친구의 친구가 몇 명인지 확인하고자
    # 친구의 범위인 1, 친구의 친구의 범위인 2에 해당되는
    # visited를 찾아 그 수를 cnt에 더해줌
    for friend in range(2, n+1):
        if 0 < visited[friend] <= 2:
            cnt += 1

    # 상근이의 결혼식에 초대하는 동기의 수 반환
    return cnt


n = int(input().rstrip())
m = int(input().rstrip())

friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    friends[a].append(b)
    friends[b].append(a)

# bfs 함수로 상근이의 결혼식에 초대하는
# 동기의 수를 찾고 이를 출력
print(bfs())