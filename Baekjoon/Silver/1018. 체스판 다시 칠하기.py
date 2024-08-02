# 1018. 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

# 맨 왼쪽 위 칸이 흰색인 체스판을 만드는 경우
# 다시 칠해야 하는 정사각형의 최수 개수를 구하는 함수
def white(i, j):
    cnt = 0
    for n in range(8):
        for m in range(8):

            # 흰색인 칸이여야 하는데 아닐 경우 cnt에 1 추가
            if (n%2 and m%2) or (not n%2 and not m%2):
                if board[i+n][j+m] != 'W':
                    cnt += 1

            # 검은색인 칸이여야 하는데 아닐 경우 cnt에 1 추가
            else:
                if board[i+n][j+m] != 'B':
                    cnt += 1

    return cnt


# 맨 왼쪽 위 칸이 검은색인 체스판을 만드는 경우
# 다시 칠해야 하는 정사각형의 최수 개수를 구하는 함수
def black(i, j):
    cnt = 0
    for n in range(8):
        for m in range(8):

            # 검은색인 칸이여야 하는데 아닐 경우 cnt에 1 추가
            if (n%2 and m%2) or (not n%2 and not m%2):
                if board[i+n][j+m] != 'B':
                    cnt += 1

            # 흰색인 칸이여야 하는데 아닐 경우 cnt에 1 추가
            else:
                if board[i+n][j+m] != 'W':
                    cnt += 1

    return cnt


N, M = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(N)]

# 최악의 경우 64칸을 전부 칠해야 하므로
# 최솟값을 구하기 위한 초기값을 64로 설정
ans = 64

# 8x8 크기의 체스판으로 잘라내기 위해
# 주어진 보드 범위 내에서 8x8 크기만큼을 탐색
for i in range(N-7):
    for j in range(M-7):

        # 체스판을 색칠하는 두 가지 경우에서
        # 다시 칠해야 하는 정사각형의 최소 개수 탐색
        white_cnt = white(i, j)
        black_cnt = black(i, j)

        # 3개의 수 중 최솟값을 ans에 갱신
        ans = min(ans, white_cnt, black_cnt)

print(ans)