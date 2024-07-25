# 17471. 게리맨더링
# https://www.acmicpc.net/problem/17471

import sys, itertools, collections
input = sys.stdin.readline

# 선거구에 포함된 구역이
# 모두 연결되어있는지 bfs 탐색으로 확인
def bfs(zone):
    qu = collections.deque()
    visited = [0] * (N+1)
    
    # 선거구에는 최소 하나의 구역이 포함되어 있으므로
    # 시작점을 첫번째 구역으로 설정
    qu.append(zone[0])
    visited[zone[0]] = 1

    while qu:
        start = qu.popleft()

        # 선거구에 포함된 구역끼리 또다른 선거구에 있는 구역을
        # 거치지 않고 연결되어 있어야 하므로
        # 탐색 범위는 선거구에 포함된 구역으로 한정
        for z in zone:

            # 만약 그 구역이 시작점과 연결되어 있고
            # 여태까지 방문하지 않았다면
            # 또다른 시작점으로 설정해 탐색을 이어감
            if z in area[start] and not visited[z]:
                qu.append(z)
                visited[z] = 1

    # 모든 탐색이 끝났음에도 방문하지 않은 곳이 있다면
    # 선거구에 포함된 구역이 모두 연결되지 않은 것이므로
    # 불가능한 방법이라는 의미로 0 반환
    for z in zone:
        if not visited[z]:
            return 0
    
    # 아닐 경우 가능한 방법이라는 의미로 1 반환
    return 1


N = int(input().rstrip())
population = list(map(int, input().rstrip().split()))

# 구역의 번호가 1부터 시작하므로 인덱스를 맞춰줌
area = [[] for _ in range(N+1)]

for i in range(1, N+1):
    info = list(map(int, input().rstrip().split()))
    M = info[0]
    for j in range(1, M+1):
        area[i].append(info[j])

# 인구 차이의 최솟값을 비교할 초기값
ans = float('inf')

# 두 선거구로 나눌 수 있는 경우의 수를 combinations으로 구현
# a, b 순서에 따른 구분이 필요없으므로
# 동일한 경우의 수가 나오는 것을 방지하기 위해 N//2+1로 범위 설정
for k in range(1, N//2+1):

    # 1~N//2 수만큼 구역을 가진 선거구들의 조합 생성
    combis = list(itertools.combinations(range(1, N+1), k))

    # 생성된 조합들 중 하나는 combi_a,
    # combi_a에 없는 구역을 combi_b로 설정
    for combi in combis:
        combi_a = combi
        combi_b = []

        for l in range(1, N+1):
            if l not in combi_a:
                combi_b.append(l)

        # 만약 a, b 모두 가능한 경우일 때
        # 인구 차이의 최솟값을 구해줌
        # 인구 수의 경우 인덱스가 0부터 시작하므로
        # 인덱스 번호에 1를 빼줌으로써 IndexError를 방지
        if bfs(combi_a) and bfs(combi_b):
            cnt_a = 0
            cnt_b = 0

            for a in combi_a:
                cnt_a += population[a-1]

            for b in combi_b:
                cnt_b += population[b-1]
            
            cnt = abs(cnt_a-cnt_b)
            ans = min(ans, cnt)

# 만약 ans가 초기값 그대로라면
# 두 선거구로 나눌 수 있는 방법이 없다는 의미이므로
# 출력 예시에 따라 -1 출력
if ans == float('inf'):
    print(-1)

# 그게 아니라면 인구 차이의 최솟값을 출력
else:
    print(ans)