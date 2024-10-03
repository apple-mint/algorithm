# 6064. 카잉 달력
# https://www.acmicpc.net/problem/6064

import sys, math
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    M, N, x, y = map(int, input().rstrip().split())
    
    # k번째가 될 수 있는 후보들 모음
    # 빠른 탐색을 위해 딕셔너리 사용
    k_dict = {}

    # 카잉 달력의 마지막 해는
    # M와 N의 최소공배수이므로
    # math 라이브러리를 사용해 이를 구함
    LCM = math.lcm(M, N)

    # x는 x가 M 미만일 경우 1씩 커지다가
    # M이 되는 순간 1로 초기화되므로
    # 주어진 x에 해당되는 k번째 후보를 다음과 같이 구함
    k = x
    while k <= LCM:
        k_dict[k] = 1
        k += M

    # y도 y가 N 미만일 경우 1씩 커지다가
    # N이 되는 순간 1로 초기화되므로
    # 위와 같이 k번째 후보를 구함
    # 만약 해당 k번째가 x에도 있다면
    # 탐색을 종료하고 해당값을 출력
    k = y
    while k <= LCM:
        if k_dict.get(k):
            print(k)
            break
        k += N

    # 만약 x의 k번째와 y의 k번째 중
    # 일치하는 것이 없는 경우
    # 유효하지 않은 표현이므로 -1 출력
    else:
        print(-1)