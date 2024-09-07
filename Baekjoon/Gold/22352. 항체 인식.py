# 22352. 항체 인식
# https://www.acmicpc.net/problem/22352

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 현재 속해 있는 칸과 같은 데이터 값을 가지면서
# 상하좌우로 인접한 칸이 있으면 백신이 퍼지므로
# 이를 확인하기 위해 bfs 함수 구현
def bfs(i, j, before_num, after_num):

    # cnt를 전역변수로 사용하고자 global 선언
    global cnt

    qu = collections.deque()

    qu.append((i, j))
    visited[i][j] = 1

    # 이전과 달라졌는지 확인 후
    # 달라졌다면 cnt에 1를 더해줌
    if before_num != after_num:
        cnt += 1

    while qu:
        si, sj = qu.popleft()

        # 상하좌우로 인접한 칸으로 이동
        for de in delta:
            ni, nj = si+de[0], sj+de[1]

            # before를 기준으로 시작점에서 인접한 칸이
            # 동일한 영역으로 묶일 수 있는지 확인
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and before[ni][nj] == before_num:
                
                # 만약 하나의 영역이라면 after도
                # 동일한 영역으로 묶일 수 있는지 확인
                # 만약 그렇다면 새로운 시작점으로 삼기 위해
                # qu에 삽입하고 방문표시를 해줌
                if after[ni][nj] == after_num:
                    qu.append((ni, nj))
                    visited[ni][nj] = 1
                
                # 만약 다르다면 하나의 영역 내에서
                # 다른 값이 존재한다는 의미이므로
                # 가능성이 없다는 것을 구분하기 위해
                # 임의의 값을 더해주고 종료
                else:
                    cnt += 99
                    return

    return


N, M = map(int, input().rstrip().split())

# 원래의 데이터 값
before = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 업데이트된 데이터 값
after = [list(map(int, input().rstrip().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

# before, after의 달라진 부분을 기록하는 변수
cnt = 0

# bfs 시작
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, before[i][j], after[i][j])

# 달라진 부분이 1개 초과일 경우
# 백신일 가능성이 없으므로 'NO' 출력
if cnt > 1:
    print('NO')

# 그렇지 않다면
# 백신일 가능성이 있으므로 'YES' 출력
else:
    print('YES')