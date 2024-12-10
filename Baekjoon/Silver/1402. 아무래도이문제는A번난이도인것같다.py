# 1402. 아무래도이문제는A번난이도인것같다
# https://www.acmicpc.net/problem/1402

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    A, B = map(int, input().rstrip().split())

    # 어떤 정수 A를 A=a1*a2*a3*...*an로 했을 때
    # A`=a1+a2+a3+...+an이 성립하면 A는 A`로 변할 수 있다고 함

    # 곱하는 임의의 수가 -1 또는 1이면
    # 제시된 범위 내 두 정수 A, B는
    # 모두 A가 B로 변할 수 있으므로 yes 출력
    print('yes')