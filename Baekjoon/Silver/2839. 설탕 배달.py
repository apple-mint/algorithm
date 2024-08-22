# 2839. 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 최대한 적은 봉지를 들고 가기 위해서는
# 5킬로그램 봉지를 최대한 많이 가져가야 하므로
# 다음과 같이 초기값 설정
five = N//5
three = (N-(5*five))//3

while True:
    
    # 주어진 5킬로그램 봉지의 개수에 5를 곱한 값과
    # 3킬로그램 봉지의 개수에 3을 곱합 값을 더한 값이
    # N킬로그램이라면 해당 봉지의 개수의 합을 출력하고 종료
    if (5*five)+(3*three) == N:
        print(five+three)
        break
    
    # 만약 아니라면 5킬로그램 봉지의 개수를 하나 줄이고
    # 그 값을 기준으로 3킬로그램 봉지의 개수를 계산
    five -= 1
    three = (N-(5*five))//3

    # 만약 5킬로그램 봉지의 개수가 음수일 경우
    # 5킬로그램 봉지를 가져갈 경우 N킬로그램을 만들 수 없으므로
    # 3킬로그램 봉지만을 가지고 N킬로그램을 만들 수 있는지 확인
    if five < 0:

        # 만들 수 있다면 봉지의 개수 출력
        if 3*three == N:
            print(three)

        # 없다면 -1 출력
        else:
            print(-1)

        # 값 출력 후 종료
        break