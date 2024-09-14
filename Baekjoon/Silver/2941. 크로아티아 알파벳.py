# 2941. 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

import sys
input = sys.stdin.readline

word = input().rstrip()
n = len(word)
cnt = 0

# 입력으로 주어진 단어의 철자를 탐색
idx = 0
while idx < n:

    # 크로아티아 알파벳은 첫 철자가
    # 'c', 'd', 'l', 'n', 's', 'z'이므로
    # 위와 같은 철자로 시작할 경우 크로아티아 알파벳인지 확인
    # 맞다면 해당 알파벳의 마지막 인덱스로 값을 갱신하기 위해
    # idx에 (해당 알파벳 길이-1)을 더해줌

    if word[idx] == 'c':
        if idx+1 < n and (word[idx+1] == '=' or word[idx+1] == '-'):
            idx += 1

    elif word[idx] == 'd':
        if idx+2 < n and word[idx+1:idx+3] == 'z=':
            idx += 2

        elif idx+1 < n and word[idx+1] == '-':
            idx += 1

    elif word[idx] == 'l' or word[idx] == 'n':
        if idx+1 < n and word[idx+1] == 'j':
            idx += 1

    elif word[idx] == 's' or word[idx] == 'z':
        if idx+1 < n and word[idx+1] == '=':
            idx += 1
    
    # cnt에 1을 더해 알파벳을 하나 셌음을 표시
    cnt += 1

    # 다음 철자로 이동
    idx += 1

# 알파벳의 수를 출력
print(cnt)