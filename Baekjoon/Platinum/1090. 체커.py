# 1090. 체커
# https://www.acmicpc.net/problem/1090

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# k개의 체커가 같은 칸에 모이도록
# 이동해야 하는 최소 횟수에 해당하는 위치는
# k개의 체커가 있는 위치 내로 범위를 좁힐 수 있으므로
# 해당하는 범위만 탐색하기 위해 각 좌표를 담을 리스트 설정
checkers, xs, ys = [], [], []

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    checkers.append((x, y))
    xs.append(x)
    ys.append(y)

ans = [float('inf')] * N

for x in xs:
    for y in ys:

        # k개의 체커가 있는 범위 내의 x, y 좌표와
        # 각 체커의 x, y좌표 사이의 거리를 계산
        cnt = []
        for cx, cy in checkers:
            cnt.append(abs(x-cx) + abs(y-cy))
        
        # 오름차순으로 계산한 거리 정렬
        cnt.sort()
        
        # 최소 횟수 순으로 k개의 체커가 같은 칸에
        # 모일 수 있도록 해당하는 k개만큼 합한 뒤
        # 해당 횟수가 최소 횟수인지 확인 후 갱신
        for k in range(N):
            ans[k] = min(ans[k], sum(cnt[0:k+1]))

print(*ans)