# 1620. 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

# 빠른 탐색을 위해 딕셔너리 사용
# names: 이름을 물어볼 때 해당 번호를 말하는 딕셔너리
# nums: 번호를 물어볼 때 해당 이름을 말하는 딕셔너리
names = {}
nums = {}

# 포켓몬 이름과 해당 이름이 나오는 순서를 짝지어
# 각각 names, nums에 기록
for num in range(1, N+1):
    name = input().rstrip()

    names[name] = num
    nums[num] = name

for _ in range(M):
    quiz = input().rstrip()

    # 만약 숫자로 물어봤다면 포켓몬의 이름 출력
    if quiz.isdigit():
        print(nums[int(quiz)])

    # 그렇지 않다면 포켓몬의 이름에 해당하는 번호 출력
    else:
        print(names[quiz])