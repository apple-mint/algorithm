# 1389. 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys, collections
input = sys.stdin.readline

# 연결된 친구 관계를 파악하고자
# bfs 함수 구현
def bfs(num):
    qu = collections.deque()
    visited = [-1] * (N+1)

    qu.append(num)
    visited[num] = 0

    while qu:
        person = qu.popleft()

        # 만약 해당 사람과 연결된 사람들 중
        # 아직 도달하지 못한 사람이 있는 경우
        # qu에 새로운 사람의 번호를 삽입하고
        # 새로운 사람의 번호에 해당되는 visited 값을
        # 기존 visited 값에 1을 더한 값으로 갱신해
        # 몇 단계를 거쳐 도달했는지를 표시
        for friend in friends[person]:
            if visited[friend] == -1:
                qu.append(friend)
                visited[friend] = visited[person] + 1

    # 인덱스 번호를 위해 맞춰준
    # visited[0]의 값이 -1이므로
    # visited의 합을 통해 구한 값에 1를 더해
    # 케빈 베이컨의 수를 만들고 이를 반환
    return sum(visited)+1


N, M = map(int, input().rstrip().split())

# 친구 관계 표시
friends = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    friends[A].append(B)
    friends[B].append(A)

ans = 0
minn = float('inf')

# 케빈 베이컨의 수가 가장 작은 사람이 여러 명일 경우
# 번호가 가장 작은 사람을 출력하기 위해
# 오름차순으로 bfs 시작
for num in range(1, N+1):
    cnt = bfs(num)

    # 만약 새로 구한 케빈 베이컨의 수가
    # 이전보다 작을 경우 그 값으로 갱신
    if cnt < minn:
        minn = cnt
        ans = num

print(ans)