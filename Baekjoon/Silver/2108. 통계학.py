# 2108. 통계학
# https://www.acmicpc.net/problem/2108

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

summ = 0
minn = 4001
maxx = -4001

nums = []
cnt = collections.defaultdict(int)

# 주어진 N개의 수로 네 가지 기본 통계값을 구하기 위해
# N개의 수들의 합, 최댓값, 최솟값, 수가 나온 횟수를 구해줌
for _ in range(N):
    num = int(input().rstrip())

    summ += num
    nums.append(num)
    cnt[num] += 1

    if num < minn:
        minn = num
    
    if num > maxx:
        maxx = num

# 소수점 이하 첫째 자리에서 반올림해 산술평균 출력
# Python round 함수는 오사오입이므로 사사오입 구현을 위해 
# 계산한 산술평균에 미세한 값을 더해주고 round 함수 사용
print(round(summ/N+10**(-10)))

# 중앙값을 구하기 위해 주어진 정수들을 정렬 후
# 그 중앙에 위치하는 중앙값 출력
nums.sort()
print(nums[N//2])

# 최빈값을 구하기 위해 N개의 수들 중
# 가장 많이 나온 순서대로 내림차순,
# 만약 나온 수가 같다면 크기가 작은 순으로 오름차순 정렬
cnt = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))

# 만약 수가 하나일 경우 그 수를 출력
if N == 1:
    print(cnt[0][0])

# 만약 수가 여러 개라면 최빈값이 여러 개 있는지 확인
else:    
    # 만약 최빈값이 여러 개라면
    # 두 번째로 작은 값 출력
    if cnt[1][1] == cnt[0][1]:
        print(cnt[1][0])

    # 최빈값이 하나라면 그 값을 출력
    else:
        print(cnt[0][0])

# 최댓값과 최솟값의 차이를 구해 범위 출력
print(abs(maxx-minn))