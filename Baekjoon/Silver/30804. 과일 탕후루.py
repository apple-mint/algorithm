# 30804. 과일 탕후루
# https://www.acmicpc.net/problem/30804

import sys
input = sys.stdin.readline

N = int(input().rstrip())
tanghulu = list(map(int, input().rstrip().split()))

fruits = {}
ans = 0
left = 0

# 막대 앞쪽에 해당하는 인덱스를 0으로 두고
# 막대 뒤쪽에 해당하는 인덱스를 0에서 뒤로 움직이며 탐색
for right in range(N):

    # 탕후루에 꽂혀있는 과일이 무엇인지 보고
    # 그 과일의 종류에 1을 더해줌
    if not fruits.get(tanghulu[right]):
        fruits[tanghulu[right]] = 1
    else:
        fruits[tanghulu[right]] += 1

    # 만약 과일을 두 종류 초과해서 썼을 경우
    # 과일을 두 종류 이하로 쓸 때까지 앞쪽 과일을 제거
    while len(fruits) > 2:
        fruits[tanghulu[left]] -= 1

        # 만약 해당 과일의 종류가 없을 경우
        # len 함수를 썼을 때 해당 과일의 종류가 세어지지 않도록
        # 해당 과일을 fruits에서 제거
        if not fruits[tanghulu[left]]:
            del fruits[tanghulu[left]]

        # 막대 앞쪽에 해당하는 인덱스에
        # 1를 더해 앞쪽 과일 제거
        left += 1

    # 과일을 두 종류 이하로 쓴 탕후루가 완성되었을 때
    # 과일의 개수가 가장 많은 탕후루인지 확인 후 값 갱신
    ans = max(ans, right-left+1)

print(ans)