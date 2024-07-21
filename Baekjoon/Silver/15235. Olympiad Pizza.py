# 15235. Olympiad Pizza
# https://www.acmicpc.net/problem/15235

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
contestants = list(map(int, input().rstrip().split()))

# 참가자가 먹어야 할 피자 조각과
# 참가자가 몇번째로 서 있는지 순서를 기록
# 리스트는 인덱스가 0부터 시작하므로 이를 고려해 설정
for i in range(N):
    contestants[i] = [contestants[i], i]

# ans: 선수별 걸린 시간을 기록
# cnt: 총 걸린 시간
ans = [0] * N
cnt = 0

# 피자를 얻기 위해 받고 다시 맨 뒤로 가므로
# 큐를 구현하기 위해 deque 사용
qu = collections.deque(contestants)

# 피자를 받기 위한 줄이 남아있을때까지 반복
while qu:
    pizza, idx = qu.popleft()

    # 피자를 한조각 주면서 1초가 걸리므로
    # 각각 변수에 해당하는 연산을 함
    pizza -= 1
    cnt += 1

    # 충분히 피자를 먹었다면
    # 참가자가 서있던 순서에 해당하는 인덱스에
    # 걸린 시간인 cnt로 값을 갱신
    if not pizza:
        ans[idx] = cnt

    # 그렇지 않다면 남은 피자 수와
    # 몇번째로 서있었는지를 다시 큐에 삽입
    else:
        qu.append([pizza, idx])

print(*ans, sep=' ')