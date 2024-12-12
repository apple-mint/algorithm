# 9019. DSLR
# https://www.acmicpc.net/problem/9019

import sys, collections
input = sys.stdin.readline

# python3으로는 시간초과,
# PyPy3는 통과된 코드

# 최소한의 명령어를 사용하기 위해 bfs 사용
def bfs(A, B):    
    qu = collections.deque()
    visited = [-1]*10000

    # 초기값 설정
    qu.append((A, ''))
    visited[A] = 0

    # bfs 시작
    while qu:
        n, command = qu.popleft()

        # 만약 변환한 수가 B와 같다면
        # 여태까지 사용한 명령어를 반환
        if n == B:
            return command

        # 네 개의 명령어 구현
        for i in range(4):

            # D 구현
            if not i:
                if n*2 > 9999:
                    result = (n*2)%10000
                else:
                    result = n*2
                
                # 만약 result에 도달하기 위해 명령어를 사용한 횟수가
                # n에 도달하기 위해 명령어를 사용한 횟수보다 작을 경우
                # 해당 명령어를 사용하는 것이 최소한의 명령어를 사용한 것이므로
                # qu에 result와 기존 명령어에서 해당 명령어를 더한 값을 삽입하고
                # n에 해당하는 visited 값에 1을 더한 값으로 값을 갱신
                if visited[result] < visited[n]:
                    qu.append((result, command+'D'))
                    visited[result] = visited[n]+1

            # S 구현
            elif i == 1:
                if not n:
                    result = 9999
                else:
                    result = n-1

                if visited[result] < visited[n]:
                    qu.append((result, command+'S'))
                    visited[result] = visited[n]+1
            
            # L 구현
            elif i == 2:
                result = (n%1000)*10 + n//1000

                if visited[result] < visited[n]:
                    qu.append((result, command+'L'))
                    visited[result] = visited[n]+1
            
            # R 구현
            else:
                result = (n%10)*1000 + n//10

                if visited[result] < visited[n]:
                    qu.append((result, command+'R'))
                    visited[result] = visited[n]+1


T = int(input().rstrip())
for _ in range(T):
    A, B = map(int, input().rstrip().split())

    # bfs를 통해 구한 최소한의 명령어 출력
    print(bfs(A, B))