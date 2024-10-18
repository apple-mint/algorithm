# 1059. 좋은 구간
# https://www.acmicpc.net/problem/1059

import sys
input = sys.stdin.readline

L = int(input().rstrip())
S = list(map(int, input().rstrip().split()))
n = int(input().rstrip())

# 집합 S에 n이 있다면
# 좋은 구간이 만들어질 수 없으므로 0이 됨
if n in S:
    cnt = 0

else:
    # 집합 S에 n이 없다면
    # n을 포함하는 구간을 살펴보기 위해
    # 집합 S를 오름차순으로 정렬하고
    # n이 속하는 집합 S 정수 내 범위 초기값을 설정
    S.sort()
    start, end = 1, 1000

    # 집합 S에 있는 모든 정수를 확인
    for x in S:

        # 만약 선택한 정수가 n보다 작다면
        # n가 속하는 집합 S 정수 내 범위의
        # 시작점이 될 수 있으므로 start 값을 갱신
        # 좋은 구간 [A, B]는 A 이상이므로
        # 선택한 정수에 1을 더한 값으로 갱신
        if x < n:
            start = x+1
        
        # 만약 선택한 정수가 n보다 크다면
        # n가 속하는 집합 S 정수 내 범위의
        # 끝점이므로 end 값을 갱신하고 종료
        # 좋은 구간 [A, B]는 B 이하이므로
        # 선택한 정수에 1을 뺀 값으로 갱신
        elif x > n:
            end = x-1
            break

    # n을 포함하는 좋은 구간은
    # n을 기준으로 좌우에 있는 숫자를
    # 몇 개 선택하는지에 따라 구할 수 있음

    # 아무것도 선택하지 않는 것도 선택이므로
    # 좌우에 있는 숫자의 개수+1를 곱해 경우의 수를 구하고
    # 어떠한 숫자도 선택하지 않았을 경우를 빼
    # 좋은 구간의 개수를 구함
    cnt = (n-start+1)*(end-n+1)-1

print(cnt)