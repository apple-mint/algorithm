# 15686. 치킨 배달
# https://www.acmicpc.net/problem/15686

import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
cities = [list(map(int, input().rstrip().split())) for _ in range(N)]

houses = []
chicken = []

# 집과 치킨집의 좌표를 확인
for r in range(N):
    for c in range(N):
        if cities[r][c] == 1:
            houses.append((r, c))

        elif cities[r][c] == 2:
            chicken.append((r, c))

# 폐업시키지 않을 치킨집을 조합을 사용해 M개 선택
combis = list(itertools.combinations(chicken, M))

# 도시의 치킨 거리의 최솟값 초기값 설정
minn = float('inf')

# 폐업시키지 않을 치킨집의
# 경우의 수를 하나하나 탐색
for combi in combis:

    # 해당 경우의 수에서 구할
    # 도시의 치킨 거리의 최솟값
    summ = 0

    # 도시에 있는 모든 집에서
    # 가장 가까운 치킨집과의 거리를 탐색
    for house in houses:
        hr, hc = house
        cnt = float('inf')

        # 선택한 집과 가장 가까운 치킨집과의
        # 거리를 구하고 이를 summ에 더해줌
        for cr, cc in combi:
            cnt = min(cnt, abs(hr-cr)+abs(hc-cc))
        summ += cnt
    
    # 구한 도시의 치킨 거리가 최솟값인지 확인 후
    # 최솟값이라면 minn을 해당 값으로 갱신
    minn = min(minn, summ)

# 구한 도시의 치킨 거리의 최솟값 출력
print(minn)