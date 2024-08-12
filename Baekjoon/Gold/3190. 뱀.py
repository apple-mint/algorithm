# 3190. 뱀
# https://www.acmicpc.net/problem/3190

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())

# 사과의 위치를 보드에 표시
# 맨 위 맨 좌측이 1행 1열이므로
# 인덱스 번호를 맞추기 위해 각 행과 열에 1를 빼줌
board = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().rstrip().split())
    board[i-1][j-1] = 1

L = int(input().rstrip())

# 주어진 방향 전환 정보를 딕셔너리에 저장
change = {}
for _ in range(L):
    X, C = input().rstrip().split()
    change[int(X)] = C

# 뱀을 deque로 표현해 뱀의 머리는 첫번째 요소,
# 뱀의 꼬리는 마지막 요소, 나머지는 몸으로 생각
snake = collections.deque()

# 초기값 설정
# 뱀은 맨위 맨좌측에 위치하므로 해당 좌표값으로 설정
snake.append((0, 0))

# 처음 오른쪽을 향하므로 move의 첫번째 요소에
# 오른쪽으로 갈 수 있게 행과 열 좌표를 설정
# 왼쪽 또는 오른쪽으로 90도 방향 회전을 하며
# 방향이 전환된다는 것을 고려하여 우, 상, 좌, 하순으로 설정
direction = 0
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]

cnt = 0
while True:
    cnt += 1

    # 뱀의 머리를 시작점으로 간주
    hi, hj = snake[0][0], snake[0][1]
    
    # 어디로 향하는지 해당되는 인덱스 번호를 조회한 뒤
    # 행과 열에 해당 값을 더해 해당 방향으로 이동
    m = move[direction]
    mi, mj = hi+m[0], hj+m[1]

    # 만약 이동한 곳이 벽이거나 자기자신의 몸일 경우 게임 종료
    if not 0<=mi<N or not 0<=mj<N or (mi, mj) in snake:
        break

    # 만약 이동한 곳에 사과가 있다면
    # 해당 사과를 먹고 사과가 없다는 의미로 0으로 갱신
    if board[mi][mj]:
        board[mi][mj] = 0
    
    # 만약 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌
    # 마지막 요소가 뱀의 꼬리이므로 pop 메서드로 제거
    else:
        snake.pop()

    # 뱀이 이동해 머리가 해당 좌표에 있으므로
    # popleft 메서드를 이용해 첫번째 요소로 추가
    snake.appendleft((mi, mj))

    # 게임 시작 시간으로부터 해당 초가 끝난 뒤
    # 방향 전환 정보가 있는지를 확인하고
    # 만약 있다면 해당 정보에 따라 방향 전환
    if change.get(cnt):
        if change[cnt] == 'L':
            if direction == 3:
                direction = 0
            else:
                direction += 1
        
        else:
            if not direction:
                direction = 3
            else:
                direction -= 1

# 게임이 몇 초에 끝나는지 출력
print(cnt)