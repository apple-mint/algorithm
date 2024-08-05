# 1107. 리모컨
# https://www.acmicpc.net/problem/1107

import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

# 만약 고장난 버튼이 있는 경우
# 주어진 고장난 버튼을 리스트에 저장
# 아닌 경우 빈 리스트로 설정
if M:
    broken = list(input().rstrip().split())
else:
    broken = []

# 만약 이동하려는 채널이 100이면
# 이동할 필요가 없으므로 0 출력
if N == 100:
    print(0)

# 만약 고장난 버튼이 없다면
# 100에서 +, - 버튼을 눌러 이동하는 것,
# 해당 숫자를 만들어 이동하는 것 둘 중 최솟값을 구해 출력
elif not M:
    print(min(abs(100-N), len(str(N))))

# 만약 이동하려는 채널이 100이 아니고
# 고장난 버튼이 있다면 가능한 경우의 수를 전부 탐색
else:

    # 버튼을 누른 최솟값의 초기값 설정
    ans = float('inf')

    # 채널이 무한대만큼 있으므로 주어진 N 중
    # 가장 큰 값인 500,000에 맞춰 전부 탐색할 수의 범위 설정
    # 500,000일 경우 버튼을 누르는 최솟값을 만들기 위해
    # 가장 크게 만들 수 있는 수는 999,999이므로 다음과 같이 범위 설정
    for n in range(1000000):

        # 해당 수의 각 자릿수를 파악하기 위해
        # 수를 문자열로 변환
        str_n = str(n)

        # 만약 해당 수를 만들기 위한 수의 버튼이 고장났을 경우
        # 시작점인 100에서 얼마만큼 눌러야 하는지를 계산
        # 계산한 cnt와 ans 중 작은 값을 ans로 갱신
        for i in range(len(str_n)):
            if str_n[i] in broken:
                cnt = abs(100-N)
                ans = min(ans, cnt)
                break

        # 만약 해당 수를 만들 수 있을 경우
        # 그 수를 시작점으로 만들기 위해 자릿수만큼 버튼을 누르고
        # 그 수에서 얼마만큼 눌러야 하는지를 계산
        # 계산한 cnt와 ans 중 작은 값을 ans로 갱신
        else:
            cnt = len(str_n) + abs(N-n)
            ans = min(ans, cnt)

    # 가능한 수를 모두 탐색하면서 얻은 최솟값 출력
    print(ans)