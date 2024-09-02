# 1343. 폴리오미노
# https://www.acmicpc.net/problem/1343

import sys
input = sys.stdin.readline

# '.'과 'X'로 이루어진 보드판에서
# 연속된 'X'가 몇 개인지 확인하기 위해
# '.'을 기준으로 나눠 입력값을 받음
board = input().rstrip().split('.')

ans = []

# 나눠진 연속된 'X' 덩어리를 탐색
for i in range(len(board)):

    X = len(board[i])
    
    # 만약 'X' 덩어리가 짝수라면
    # 'AAAA', 'BB'로 덮을 수 있으므로 그 수를 계산
    if not X % 2:

        # 사전순으로 가장 앞서는 답을 만들기 위해
        # 'X'를 'AAAA'로 덮을 수 있는 만큼 먼저 덮음
        a = 4 * (X//4)

        # 남은 'X'를 'BB'로 덮음
        b = X - a

        # 폴리오미노로 덮은 것을 ans에 삽입
        ans.append('A'*a+'B'*b)

    # 만약 홀수라면 덮을 수 없으므로
    # ans를 빈 리스트로 만들고 탐색 종료
    else:
        ans = []
        break

# 만약 ans에 값이 있다면
# 폴리오미노로 모두 덮은 보드판을 출력
# 덩어리 사이에 '.'이 출력되도록 다음과 같이 작성
if ans:
    print(*ans, sep='.')

# 만약 ans에 값이 없다면
# 덮을 수 없는 것이므로 -1 출력
else:
    print(-1)