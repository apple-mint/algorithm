# 9375. 패션왕 신해빈
# https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())

    # 한 종류에 의상이 몇 개 있는지를 기록
    clothes = {}
    for _ in range(n):
        name, kind = input().rstrip().split()

        # 해당 종류가 처음 나왔을 경우 keyerror를 방지하고자
        # 다음과 같이 초기값을 설정
        if not clothes.get(kind):
            clothes[kind] = 0

        clothes[kind] += 1

    # 의상의 종류 중 하나를 선택하여
    # 돌아다니는 경우를 구하는 것이므로
    # 아무것도 선택하지 않은 경우 + 해당 종류의 의상 수를 곱해줌
    ans = 1
    for cnt in clothes.values():
        ans *= (cnt+1)
    
    # 모든 것을 선택하지 않는 경우가 발생하므로
    # 이를 제외하고 의상을 입을 수 있는 경우 출력
    # 이럴 경우 만약 의상의 수가 0인 경우
    # 1-1 = 0이 되어 답이 나오므로 예외처리를 해줄 필요가 없음
    print(ans-1)