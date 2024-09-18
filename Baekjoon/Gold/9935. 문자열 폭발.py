# 9935. 문자열 폭발
# https://www.acmicpc.net/problem/9935

import sys
input = sys.stdin.readline

word = list(input().rstrip())
bomb = list(input().rstrip())

# 매번 끝에서부터 폭탄 문자열의 길이만큼
# 문자를 가져와 문자열을 만드므로
# 하나의 stack만으로도 답을 구할 수 있음
stack = []

for i in range(len(word)):

    # 문자열에 있는 문자를 stack에 삽입
    stack.append(word[i])

    # 폭탄 문자열이 완성되었는지 확인하기 위해
    # stack의 마지막에서부터 폭탄 문자열의 길이까지의 문자로
    # 문자열을 만든 뒤 이가 bomb와 같은지를 확인
    if stack[len(stack)-len(bomb):] == bomb:

        # 만약 같다면 해당 문자열 제거
        for _ in range(len(bomb)):
            stack.pop()

# 만약 stack에 남아있는 문자가 있다면
# 남아있는 문자 출력
if stack:
    print(*stack, sep='')

# 아니라면 FRULA 출력
else:
    print('FRULA')