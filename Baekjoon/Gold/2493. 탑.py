# 2493. 탑
# https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

N = int(input().rstrip())
towers = list(map(int, input().rstrip().split()))

# 각 탑이 몇 번째 있는지
# 확인하기 위해 인덱스 정보 추가
for i in range(N):
    towers[i] = (towers[i], i+1)

ans = [0] * (N+1)
stack = []

# 가장 오른쪽에 있는 탑부터 레이저 신호를 발사했을 때
# 어느 탑에서 수신하는지를 모두 탐색
while towers:

    # 탑 하나를 선택
    tower, tower_idx = towers.pop()

    # 현재 선택한 탑이 오른쪽에 있었던 탑보다
    # 높이가 높아 이전의 레이저 신호를 수신할 수 있는지 확인
    while stack:
        pre, pre_idx = stack.pop()

        # 만약 현재 선택한 탑의 높이가 더 낮다면
        # stack을 원래대로 되돌려놓은 뒤에 종료
        if tower < pre:
            stack.append((pre, pre_idx))
            break
        
        # 현재 선택한 탑의 높이가 높다면
        # 레이저 신호를 수신한 탑의 정보를 갱신
        ans[pre_idx] = tower_idx
    
    # 선택한 탑의 레이저 신호를
    # 수신할 수 있는 탑이 왼쪽에 있는지
    # 확인하기 위해 stack에 해당 탑의 정보 삽입
    stack.append((tower, tower_idx))

print(*ans[1:])