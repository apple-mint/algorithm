# 1541. 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

# 식의 값을 최소로 만들기 위해서는
# 음수값을 최대로 만들어야 하므로
# '-' 뒤에 있는 양수들을 전부 음수로 바꾸면 됨

# '-'를 기준으로 나눠 하나의 숫자와 양수값들의 모음으로 구분
expression = input().rstrip().split('-')

ans = 0
for i in range(len(expression)):

    # 만약 숫자로 바꿀 수 있는 값일 경우
    # 하나의 숫자이므로 위치에 따라 적절한 연산을 해줌
    if expression[i].isdigit():

        # 만약 첫 번째 요소일 경우 앞에
        # 연산자가 없는 양수이므로 ans에 값을 더해줌
        if not i:
            ans += int(expression[i])

        # 그렇지 않을 경우 앞에 '-' 연산자가 있는
        # 음수이므로 ans에 값을 빼줌
        else:
            ans -= int(expression[i])

    # 만약 숫자로 바꿀 수 없는 경우 양수값들의 모음이므로
    # '+'를 기준으로 나눠 해당 식을 구성하고 있던
    # 양수들을 숫자로 변환해 nums에 저장
    else:
        nums = list(map(int, expression[i].split('+')))

        # 만약 ans가 양수라면 nums 앞에
        # '-' 연산자가 있는 것이므로 ans에 nums의 합을 뺴줌
        if ans:
            ans -= sum(nums)

        # 만약 아니라면 nums 앞에
        # '-' 연산자가 없는 것이므로 ans에 nums의 합을 더해줌
        else:
            ans += sum(nums)

print(ans)