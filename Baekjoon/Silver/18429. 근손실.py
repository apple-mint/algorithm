# 18429. 근손실
# https://www.acmicpc.net/problem/18429

import sys
input = sys.stdin.readline

# 어떤 시점에서라도 중량이 500보다 크거나 같아야 하므로
# 이를 만족하는 경우의 수만 고려하기 위해 백트래킹 함수 구현
def backtracking(weight, cnt):

    # 설정한 초기값을 사용하기 위해
    # global 선언
    global ans

    # N개의 운동 키트를 사용했다면
    # 운동 기간동안 항상 중량이 500 이상인 순서로
    # 운동 키트를 적용했다는 의미이므로
    # ans에 1을 더하고 탐색 종료
    if cnt == N:
        ans += 1
        return
    
    # N개의 운동 키트에서 아직 사용하지 않은 운동 키트 중
    # 중량이 K만큼 감소해도 해당 운동 키트를 사용하면
    # 중량이 500 이상으로 유지되는 것을 선택
    for num in range(N):
        if not visited[num] and weight+kits[num]-K >= 500:

            # 적용한 운동 키트임을 표시해주고
            # 다음 사용할 운동 키트를 확인하기 위해
            # 중량과 사용 횟수를 갱신하고 함수 호출
            visited[num] = 1
            backtracking(weight+kits[num]-K, cnt+1)

            # 탐색이 끝났으면 다음 경우의 수를 찾기 위해
            # 해당 운동 키트를 적용하지 않은 상태로 초기화
            visited[num] = 0


N, K = map(int, input().rstrip().split())
kits = list(map(int, input().rstrip().split()))

# 백트래킹을 위한 초기값 설정
ans = 0
visited = [0]*N

# 백트래킹 시작
backtracking(500, 0)

# 구한 경우의 수 출력
print(ans)