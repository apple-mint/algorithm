# 1929. 소수 구하기
# https://www.acmicpc.net/problem/1929

import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())

# 인덱스 번호가 소수일 경우 1,
# 아닐 경우 0 값을 가지는 리스트의 초기값 설정
is_prime = [1]*(N+1)

# 0과 1은 소수가 아니므로 0으로 값 갱신
is_prime[0] = 0
is_prime[1] = 0

# 2부터 N까지 해당 숫자가 소수인지를 확인
for p in range(2, N+1):

    # 만약 p가 소수인 경우
    # p를 제외한 p의 배수는 소수가 아니므로
    # p에 2를 곱하는 것을 시작으로
    # N을 초과하기 전까지 수를 하나씩 늘려 곱해줘
    # p를 제외한 p의 배수를 구하고
    # 소수가 아니라는 의미로 0으로 값 갱신
    if is_prime[p]:
        m = 2
        while p*m < N+1:
            is_prime[p*m] = 0
            m += 1

# M 이상 N 이하 내 소수를 탐색하고
# 소수이면 해당 값을 출력
for num in range(M, N+1):
    if is_prime[num]:
        print(num)