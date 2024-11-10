# 1987. 알파벳
# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline

# python3으로는 시간초과,
# PyPy3는 통과된 코드

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(sr, sc, cnt):

    # 최대의 칸 수 기록을 위해
    # global 선언으로 maxx 변수 사용
    global maxx

    # 말을 상하좌우로 인접한 칸 중 하나로 이동
    for d in delta:
        nr, nc = sr+d[0], sc+d[1]
        
        # 이동한 칸이 보드 내에 있고 방문하지 않았다면
        # 해당 칸 알파벳이 지금까지 지나온 칸의 알파벳과 다른지 확인
        if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
            if board[nr][nc] not in alphabet:

                # 만약 다르다면 해당 칸을 지날 수 있으므로
                # alphabet에 해당 칸 알파벳을 추가하고
                # 해당 칸을 방문표시하고 이동한 칸 수에 1을 더해준 뒤
                # dfs 함수를 호출해 더 이동할 수 있는지를 확인
                alphabet.add(board[nr][nc])
                visited[nr][nc] = 1
                dfs(nr, nc, cnt+1)

                # 다른 이동할 수 있는 경우를 탐색하기 위해
                # alphabet, visited 상태를 이전으로 되돌림
                alphabet.remove(board[nr][nc])
                visited[nr][nc] = 0

    # dfs 함수 호출 없이 for문이 끝났다면
    # 해당 경우의 수에서 최대한으로 이동한 것이므로
    # 지나온 칸 수가 최대인지 확인 및 갱신 후 종료
    maxx = max(maxx, cnt)
    return


R, C = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]

maxx = 0
alphabet = set()
visited = [[0]*C for _ in range(R)]

# 말은 좌측 상단 칸에서 시작하므로
# 해당 칸으로 초기값 설정
alphabet.add(board[0][0])
visited[0][0] = 1

# dfs 시작
dfs(0, 0, 1)

# 말이 지날 수 있는 최대의 칸 수 출력
print(maxx)