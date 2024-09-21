# 2960. 에라토스테네스의 체
# https://www.acmicpc.net/problem/2960

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

# 인덱스 번호가 지워지지 않았다면 1,
# 지워졌다면 0 값을 가지는 리스트의 초기값 설정
nums = [1]*(N+1)

# 수를 몇 개 지웠는지 확인하기 위한 변수
cnt = 0

# 문제의 요구사항에 따라
# 에라토스테네스의 체 알고리즘 구현
for n in range(2, N+1):

    # 만약 K개만큼 수를 지운 경우
    # 수를 찾아 지우는 것을 종료
    if cnt == K:
        break
    
    # 아직 지우지 않은 수 중
    # 가장 작은 수를 찾아 이를 p라고 함
    if nums[n]:

        # p부터 아직 지우지 않은 p의 배수를
        # 인덱스 번호로 가진 nums[p]를
        # 0으로 값을 바꾸는 것으로 수를 지우며
        # 수를 지울 때마다 cnt에 1을 더해줌
        for p in range(n, N+1, n):
            if nums[p]:
                nums[p] = 0
                cnt += 1

            # 만약 K개만큼 수를 지운 경우
            # K번째 지워진 수를 ans에 저장하고
            # 수를 찾아 지우는 것을 종료
            if cnt == K:
                ans = p
                break

# K번째 지워진 수를 출력
print(ans)