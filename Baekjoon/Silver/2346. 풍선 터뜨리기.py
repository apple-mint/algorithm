# 2346. 풍선 터뜨리기
# https://www.acmicpc.net/problem/2346

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

# 양수, 음수에 따라 이동 방향이 다르므로
# 이를 구현하기 위해 deque 사용
balloons = collections.deque()

# 터진 풍선의 번호를 나열하기 위해
# 종이에 적혀 있는 수와 함께 풍선의 번호 저장
for i in range(N):
    balloons.append((i+1, nums[i]))

# 터진 풍선의 번호를 담을 리스트
ans = []

# 규칙에 따라 풍선을 터뜨리기 시작
while True:

    # 터진 풍선 안에 있는 수와
    # 터진 풍선의 번호를 변수에 저장
    idx, num = balloons.popleft()

    # 터진 풍선의 번호를 ans에 삽입
    ans.append(idx)

    # 만약 풍선이 다 터졌을 경우
    # 터뜨리는 것을 종료
    if not balloons:
        break

    # 만약 터진 풍선 안에 있는 수가 양수일 경우
    # 그 절댓값만큼 오른쪽으로 이동하므로
    # 맨 앞에 있는 풍선을 맨 뒤로 보냄으로써 이를 구현
    # 풍선이 터지면서 이동해야 할 풍선 하나가
    # 이미 맨 앞에 있는 상태이므로 절댓값보다 하나 더 적게 이동
    if num > 0:
        for _ in range(num-1):
            balloons.append(balloons.popleft())
            pass

    # 만약 터진 풍선 안에 있는 수가 음수일 경우
    # 그 절댓값만큼 왼쪽으로 이동하므로
    # 맨 뒤에 있는 풍선을 맨 앞으로 보냄으로써 이를 구현
    else:
        for _ in range(-num):
            balloons.appendleft(balloons.pop())
            pass

# 출력 예시에 따라 터진 풍선의 번호 출력
print(*ans)