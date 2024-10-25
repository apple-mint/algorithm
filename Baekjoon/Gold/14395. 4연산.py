# 14395. 4연산
# https://www.acmicpc.net/problem/14395

import sys, collections
input = sys.stdin.readline

# 연산의 아스키 코드 순으로 연산했을 때
# 최소 연산 횟수를 찾기 위해 bfs 구현
def bfs(num):

    qu = collections.deque()

    # 숫자 s, t의 범위가 1부터 10**9까지이므로
    # KeyError 없이 빠른 탐색이 가능한
    # 딕셔너리의 특성을 활용하고자 defaultdict 사용
    visited = collections.defaultdict(int)

    # bfs 시작을 위한 초기값 설정
    qu.append((num, ''))
    visited[num] = 1

    # bfs 시작
    while qu:
        n, ans = qu.popleft()

        # 만약 t와 같을 경우
        # 여태까지 연산한 연산자를 반환
        if n == t:
            return ans

        # 사전 순으로 앞서는 것을 출력하기 위해
        # *, +, / 순으로 연산할 수 있도록 함
        # - 연산은 하게 되면 그 값이 0으로 고정되고
        # 숫자 s와 t의 범위는 자연수이므로 - 연산 제외

        # 연산을 했을 때 그 결과가 t 이내이고 처음 나온 수라면
        # qu에 삽입하고 이를 기준으로 다시 연산할 수 있게 하고
        # visited에 방문표시를 해 중복해서 연산하는 일을 방지함
    
        if n*n<=t and not visited[n*n]:
            qu.append((n*n, ans+'*'))
            visited[n*n] = 1

        if n+n<=t and not visited[n+n]:
            qu.append((n+n, ans+'+'))
            visited[n+n] = 1

        if n//n<=t and not visited[n//n]:
            qu.append((n//n, ans+'/'))

    # 도중에 반환되지 않고 while문이 끝났다면
    # 바꿀 수 없는 경우이므로 -1을 반환
    return -1


s, t = map(int, input().rstrip().split())

# s와 t가 같은 경우
# 연산이 필요 없으므로 0 출력
if s == t:
    print(0)

# s와 t가 다를 경우
# 4연산을 하고 나온 결과값을 출력
else:
    print(bfs(s))