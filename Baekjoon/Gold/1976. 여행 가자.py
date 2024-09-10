# 1976. 여행 가자
# https://www.acmicpc.net/problem/1976

import sys, collections
input = sys.stdin.readline

# 여행 계획에 속한 도시들끼리
# 연결되었는지 확인하기 위해 bfs 진행
def bfs(start):
    qu = collections.deque()
    visited = [0]*N

    # 방문한 여행 계획에 속한 도시의 수
    cnt = 1

    qu.append(start)
    visited[start] = 1

    # bfs 시작
    while qu:
        city = qu.popleft()

        # 만약 여행 계획에 속한 모든 도시에 방문했다면
        # 가능한 여행 계획이므로 True 반환
        if cnt == M:
            return True
        
        # 출발지와 연결된 도시이면서
        # 아직 방문하지 않은 도시인 경우,
        for num in range(N):
            if connected[city][num] and not visited[num]:

                # 만약 방문한 도시가
                # 여행 계획에 속해 있다면
                # cnt에 1을 더해줌
                if num in cities:
                    cnt += 1

                # 여행 계획에 속한 도시인지와 상관없이
                # 방문한 도시를 새로운 출발지로 삼고자
                # qu에 도시 번호를 삽입하고 방문 표시를 함
                qu.append(num)
                visited[num] = 1

    # 도중에 함수가 종료되지 않았다면
    # 여행 계획에 속한 모든 도시에
    # 방문하지 못한 것이므로 False 반환
    return False


N = int(input().rstrip())
M = int(input().rstrip())

# 각 도시들의 연결 정보
connected = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 여행 계획에 속한 도시들의 번호에
# 1을 빼 도시의 연결 정보와 도시 번호를 맞춰줌
cities = list(map(int, input().rstrip().split()))
for i in range(M):
    cities[i] -= 1

# 중간에 다른 도시를 경유할 수도 있고
# 같은 도시에 여러 번 방문해도 되므로
# 여행 계획 순서에 상관없이 출발지에서 출발했을 때
# 모든 도시에 적어도 한번씩 방문할 수 있다면 가능한 여행 계획임

# 출발지 설정
start = cities[0]

# 중복된 도시 번호 제거 후
# 여행 계획에 속한 도시들의 수를 갱신
cities = set(cities)
M = len(cities)

# bfs 결과에 따라 알맞은 값 출력
if bfs(start):
    print('YES')
else:
    print('NO')