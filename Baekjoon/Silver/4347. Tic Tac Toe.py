# 4347. Tic Tac Toe
# https://www.acmicpc.net/problem/4347

import sys
input = sys.stdin.readline

# 'X' 또는 'O'가 몇 개의 줄을 완성했는지
# symbol에 따라 그 수를 세 반환하는 함수
def check_line(symbol):
    cnt = 0

    for i in range(3):
        if symbol == board[i][0] == board[i][1] == board[i][2]:
            cnt += 1
    
    for j in range(3):
        if symbol == board[0][j] == board[1][j] == board[2][j]:
            cnt += 1

    if symbol == board[0][0] == board[1][1] == board[2][2]:
        cnt += 1
    
    if symbol == board[0][2] == board[1][1] == board[2][0]:
        cnt += 1

    return cnt


# 유효한 틱택토인지 확인하는 함수
def is_valid(symbol):

    # 'X' 또는 'O'가 몇 개의 줄을 완성했는지
    # 함수를 통해 확인 후 그 수를 저장
    x_line = check_line('X')
    o_line = check_line('O')

    # 만약 틱택토가 'X', 'O'로만 이루어져 있고
    # 'X'가 'O'보다 1개 더 많을 때
    # 'X'가 이기거나 비긴 상태로 게임이 끝난 상황이여야
    # 유효한 틱택토이므로 다음과 같은 조건을 만족할 때 'yes' 반환

    # 해당 경우 'X'가 5개이므로
    # XOX       다음과 같은 경우가 가능하므로
    # OXO       범위를 0 이상 2 이하로 정함
    # XOX
    if not cnt_dot and symbol == 'X':
        if 0<=x_line<=2 and not o_line:
            return 'yes'
    
    # 만약 틱택토에 빈 칸이 있고 'X'가 'O'보다 1개 더 많을 때
    # 'X'가 이겨 게임이 끝나거나 게임이 진행 중인 상황이여야
    # 유효한 틱택토이므로 다음과 같은 조건을 만족할 때 'yes' 반환
    elif cnt_dot and symbol == 'X':
        if 0<=x_line<=1 and not o_line:
            return 'yes'
    
    # 만약 틱택토에 빈 칸이 있고 'O'가 'X'의 수가 같을 때
    # 'O'가 이겨 게임이 끝나거나 게임이 진행 중인 상황이여야
    # 유효한 틱택토이므로 다음과 같은 조건을 만족할 때 'yes' 반환
    elif cnt_dot and symbol == 'O':
        if not x_line and 0<=o_line<=1:
            return 'yes'
    
    # 그 외의 경우 유효한 틱택토가 아니므로 'no' 출력
    return 'no'


N = int(input().rstrip())
for n in range(1, N+1):
    board = [list(input().rstrip()) for _ in range(3)]

    cnt_X = 0
    cnt_O = 0
    cnt_dot = 0

    # 틱택토에 나오는 'X', 'O', '.'의 개수를 세줌
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                cnt_X += 1
            elif board[i][j] == 'O':
                cnt_O += 1
            else:
                cnt_dot += 1
    
    # 'X'가 선공이므로 'X'가 'O'보다 1개 더 많을 때
    # 유효한 틱택토인지 함수를 통해 확인 후 그 결과를 출력
    if cnt_X == cnt_O+1:
        print(is_valid('X'))

    # 'O'가 후공이므로 'O'가 'X'의 수가 같을 때
    # 유효한 틱택토인지 함수를 통해 확인 후 그 결과를 출력
    elif cnt_X == cnt_O:
        print(is_valid('O'))

    # '.'이 9개일 경우 아직 게임을 시작하지 않은 것이므로
    # 유효한 틱택토로 간주해 'yes' 출력
    elif cnt_dot == 9:
        print('yes')

    # 그 외의 경우 유효한 틱택토가 아니므로 'no' 출력
    else:
        print('no')

    # 한 줄 띄어쓰기 후 새로운 테스트케이스가 입력되므로
    # 마지막 입력이 아닐 경우 한줄을 입력받을 수 있도록 함
    if n != N:
        _ = input().rstrip()