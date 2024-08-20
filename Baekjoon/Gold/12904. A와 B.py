# 12904. A와 B
# https://www.acmicpc.net/problem/12904

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

# S에 두 가지 연산을 하며 T로 바꾸면 시간초과가 나므로
# T에서 했던 연산을 되돌리며 바꿀 수 있는지를 확인
while T:

    # 만약 T가 S가 되었다면
    # 바꿀 수 있으므로 1을 출력하고 종료
    if T == S:
        print(1)
        break

    # 1. 문자열 뒤에 'A' 추가,
    # 2. 문자열을 뒤집고 뒤에 'B' 추가하는
    # 두 연산을 되돌리는 것이므로
    # 동일하게 뒤에 있는 문자열을 제거해주고
    # 만약 그 문자열이 'B'라면 문자열을 뒤집어줌
    if T.pop() == 'B':
        T.reverse()

# T가 빈 문자열이 될 때까지 종료되지 않았다면
# 바꿀 수 없는 경우이므로 0을 출력
else:
    print(0)