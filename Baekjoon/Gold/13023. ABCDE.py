# 13023. ABCDE
# https://www.acmicpc.net/problem/13023

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# A->B->C->D->E와 같은
# 친구 관계가 있는지 확인하는 함수
def dfs(start, cnt):

    # 재귀함수 형태이므로
    # 값을 보존하기 위해 global 선언
    global is_valid

    # cnt가 A, B, C, D, E의 수인 5라면
    # 친구 관계가 있는 것이므로
    # is_valid 값을 갱신 후 종료
    if cnt == 5:
        is_valid = True
        return

    # 해당 사람과 연결되어 있는 친구 중
    # 아직 확인하지 않은 친구가 있다면
    # 확인하지 않은 친구 확인표시 후
    # 확인하지 않은 친구의 번호, cnt에 1를 더한 값으로 dfs 호출
    # dfs 함수가 종료되었다면 다음 탐색을 위해 확인표시 초기화
    for friend in friends[start]:
        if not visited[friend]:
            visited[friend] = 1
            dfs(friend, cnt+1)
            visited[friend] = 0
    
    return


N, M = map(int, input().rstrip().split())

# 친구 관계 표시
friends = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    friends[a].append(b)
    friends[b].append(a)

# 확인 여부 표시
visited = [0]*N

# 친구 관계가 있는지 표시
is_valid = False

for start in range(N):

    # 해당 사람 확인표시
    visited[start] = 1

    # 1대1로 쭉 이어지는 관계가 있는지 확인해야 하므로
    # 하나의 정점으로부터 쭉 내려가 탐색하는 dfs 사용
    dfs(start, 1)

    # 다음 탐색을 위해 값 초기화
    visited[start] = 0

    # 만약 친구 관계를 찾았다면
    # 더 탐색할 필요가 없으므로 종료
    if is_valid:
        break

# 친구 관계 유무에 따라 값 출력
if is_valid:
    print(1)
else:
    print(0)