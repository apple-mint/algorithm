# 17413. 단어 뒤집기 2
# https://www.acmicpc.net/problem/17413

import sys
input = sys.stdin.readline

S = input().rstrip()

# 뒤집을 단어를 보관할 stack
stack = []

# 문자열 S에서 단어만 뒤집은 결과
ans = []

# 문자열 S를 구성하는 철자를 탐색
idx = 0
while idx < len(S):

    # '<'이면 태그이므로
    # 뒤집지 않고 그대로 출력
    if S[idx] == '<':

        # '<'가 시작되면 하나의 단어가 끝나므로
        # stack에 뒤집어야 하는 단어가 있을 경우
        # 나중에 들어온 순서대로 ans에 삽입 후 초기화
        for _ in range(len(stack)):
            ans.append(stack.pop())
        stack = []

        # 현재 인덱스를 시작점으로 삼고
        # '>'가 나올 때까지 쭉 이동해
        # 태그가 어디서부터 어디인지를 확인
        start = idx
        while S[idx] != '>':
            idx += 1

        # 구한 태그를 그대로 ans에 삽입
        ans.append(S[start:idx+1])

    # 공백일 경우 하나의 단어가 끝났음을 의미하므로
    # stack에 뒤집어야 하는 단어가 있을 경우
    # 나중에 들어온 순서대로 ans에 삽입 후 초기화
    elif S[idx] == ' ':
        for _ in range(len(stack)):
            ans.append(stack.pop())
        ans.append(' ')
        stack = []

    else:
        # 알파벳 소문자, 숫자라면 나중에 들어온 순서대로
        # 뺌으로써 뒤집은 단어를 구현하기 위해 stack에 삽입
        stack.append(S[idx])

        # 문자열의 마지막이라면 하나의 단어가 끝난 것이므로
        # stack에 뒤집어야 하는 단어가 있을 경우
        # 나중에 들어온 순서대로 ans에 삽입 후 초기화
        if idx == len(S)-1:
            for _ in range(len(stack)):
                ans.append(stack.pop())
            stack = []
    
    # 다음 인덱스로 이동
    idx += 1

# 출력 예시에 따라
# 재구성한 문자열 S를 출력
print(*ans, sep='')