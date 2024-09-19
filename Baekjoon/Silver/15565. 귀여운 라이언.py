# 15565. 귀여운 라이언
# https://www.acmicpc.net/problem/15565

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dolls = list(map(int, input().rstrip().split()))

# 라이언 인형이 몇 개인지,
# 어디에 있는지 확인하기 위해
# 라이언 인형의 인덱스를 저장
lion = []
for i in range(N):
    if dolls[i] == 1:
        lion.append(i)

# 라이언 인형이 K개 이상 있는 연속된 인형들의
# 집합의 크기의 최솟값을 구하기 위한 초기값
ans = N+1

# K개 이상의 라이언 인형이 집합 내에 있어야 하므로
# 라이언 인형이 K개 이상이여야 집합이 존재할 수 있음
if len(lion) >= K:

    # 집합 하나에 라이언 인형이 K개가 되어야
    # 가장 작은 연속된 인형들의 집합을 만들 수 있으므로
    # 앞에서부터 차례로 K개만큼 선택해 크기를 구해주고
    # 구한 크기가 최솟값인지를 비교해 ans 갱신
    for i in range(len(lion)-K+1):
        cnt = lion[i+K-1]-lion[i]+1
        ans = min(ans, cnt)
    
    # 구한 연속된 인형들의
    # 집합의 크기의 최솟값을 출력
    print(ans)

# 만약 K보다 작다면 그런 집합이
# 없다는 것이므로 -1 출력
else:
    print(-1)