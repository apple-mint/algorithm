# 16953. A → B
# https://www.acmicpc.net/problem/16953

import sys, collections
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

# bfs를 통해 연산의 최솟값을 구해줌
# popleft 메서드가 필요하므로 deque 사용
qu = collections.deque()

# 해당 수는 최소 몇 번의 연산을 해야 하는지 표시
# 빠른 탐색을 위해 딕셔너리 사용
cnt = {}

# bfs를 위한 초기설정
qu.append(A)
cnt[A] = 1

# bfs 시작
while qu:

    # qu 안에 담긴 초기값
    x = qu.popleft()

    # 만약 x가 B와 같다면
    # A를 B로 바꾼 것이므로 종료
    if x == B:
        break
    
    # x가 B보다 클 경우 더이상 의미가 없으므로
    # x가 B보다 작을 경우에만 두 가지 연산 진행
    elif x < B:

        # 2를 곱하는 연산을 했을 때 나온 값이
        # 이 경우를 통해서 처음 나온 경우
        # qu에 해당 값을 넣어주고
        # cnt에 그 값이 몇 번째로 나왔는지 표시
        if not cnt.get(x*2):
            qu.append(x*2)
            cnt[x*2] = cnt[x]+1
        
        # 1을 수의 가장 오른쪽에 추가한 연산을 했을 때
        # 나온 값이 이 경우를 통해서 처음 나온 경우
        # qu에 해당 값을 넣어주고
        # cnt에 그 값이 몇 번째로 나왔는지 표시
        if not cnt.get(int(str(x)+'1')):
            qu.append(int(str(x)+'1'))
            cnt[int(str(x)+'1')] = cnt[x]+1

# 모든 탐색이 끝났을 경우 B가 몇 번째에 나왔는지 출력
# 만약 그 값을 찾을 수 없는 경우 만들 수 없는 경우이므로 -1 출력
print(cnt.get(B, -1))