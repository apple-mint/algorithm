# 2210. 숫자판 점프
# https://www.acmicpc.net/problem/2210

import sys
input = sys.stdin.readline

# 인접해 있는 네 방향으로 움직이기 위한 좌표
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 시작칸에서 인접해 있는 네 방향으로 이동하며
# 6자리의 수를 만들기 위해 dfs 구현
def dfs(si, sj, num, cnt):

    # 만약 다섯 번 모두 이동했을 경우
    # 만들어진 숫자를 ans에 추가하고 종료
    if cnt == 5:
        ans.add(num)
        return

    # 시작칸을 기준으로 인접해 있는 네 방향으로 이동
    for d in delta:
        ni = si + d[0]
        nj = sj + d[1]

        # 만약 이동한 칸이 숫자판 범위 내에 있다면
        # 해당 칸을 새로운 시작칸으로 삼기 위해
        # 적절한 값을 dfs 함수에 넘겨주며 호출
        if 0<=ni<5 and 0<=nj<5:
            dfs(ni, nj, num+board[ni][nj], cnt+1)


board = [(input().rstrip().split()) for _ in range(5)]

# 중복된 수를 제거하기 위해 집합 사용
ans = set()

# 모든 칸을 탐색하며 해당 칸에서
# 인접해 있는 네 방향으로 이동해
# 만들 수 있는 6자리의 수를 찾고 그 값을 저장
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j], 0)

# 만들 수 있는 수들의 개수 출력
print(len(ans))