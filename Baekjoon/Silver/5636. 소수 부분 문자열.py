# 5636. 소수 부분 문자열
# https://www.acmicpc.net/problem/5636

import sys
input = sys.stdin.readline

nums = [0] * 100001
is_prime = []

# 부분 문자열에서 가장 큰 소수를 찾기 위해
# 2보다 크거나 같고 100,000보다 작거나 같은 소수를 구함
for num in range(2, 100001):
    if not nums[num]:
        nums[num] = 1
        is_prime.append(num)

        cnt = 2
        while cnt*num <= 100000:
            nums[cnt*num] = 1
            cnt += 1

# while문으로 여러 개의 테스트 케이스를 입력받음
while True:
    words = input().rstrip()

    # 0이 들어왔을 경우 테스트 케이스 종료
    if words == '0':
        break

    # 빠른 탐색을 위해 가장 큰 수부터 시작해
    # 해당 소수를 문자열로 바꿔
    # 입력 문자열에 있는지 확인 후
    # 있다면 해당 소수를 출력하고 탐색 종료
    for i in range(len(is_prime)-1, -1, -1):
        if str(is_prime[i]) in words:
            print(is_prime[i])
            break