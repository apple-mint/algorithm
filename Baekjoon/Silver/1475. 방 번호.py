# 1475. 방 번호
# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

# 자릿수 하나씩 탐색하기 위해 문자열로 입력값을 받음
N = input().rstrip()

# nums의 인덱스 번호는 0~9까지 설정해
# 나온 숫자와 인덱스 번호를 맞춰줌으로써
# 숫자가 얼마나 나왔는지를 계산
nums = [0] * 10
for i in range(len(N)):
    nums[int(N[i])] += 1

# 6은 9로, 9는 6으로 이용할 수 있으므로
# 하나의 세트에서 이용할 수 있는 개수가 2개가 됨
# 따라서 두 숫자가 나온 개수의 합을 2로 나눠 값을 새로 갱신
 
# 두 숫자의 합이 2로 나누었을 때 나머지가 있는 경우
# 세트 하나가 부족하므로 이를 추가해 값을 갱신
if (nums[6]+nums[9]) % 2:
    nums[6] = (nums[6]+nums[9])//2 + 1
    nums[9] = 0

# 나누어 떨어진다면 그 몫으로 값을 갱신
else:
    nums[6] = (nums[6]+nums[9])//2
    nums[9] = 0

# 필요한 세트의 개수의 최솟값을 구하기 위해
# 가장 많이 나온 숫자를 기준으로 개수 출력
print(max(nums))