# 14405. 피카츄
# https://www.acmicpc.net/problem/14405

import sys
input = sys.stdin.readline

S = input().rstrip()
is_pikachu = False

idx = 0
while idx < len(S):

    # 'p'로 시작될 때 'pi'인지 확인하고
    # 맞다면 다음을 탐색하기 위해 그 글자수만큼 idx에 더해줌
    # 만약 아니라면 발음할 수 있는 문자열이 아니므로 종료
    if S[idx] == 'p':
        if idx+1 < len(S) and S[idx+1] == 'i':
            idx += 2
        else:
            break

    # 'k'로 시작될 때 'ka'인지 확인하고
    # 맞다면 다음을 탐색하기 위해 그 글자수만큼 idx에 더해줌
    # 만약 아니라면 발음할 수 있는 문자열이 아니므로 종료
    elif S[idx] == 'k':
        if idx+1 < len(S) and S[idx+1] == 'a':
            idx += 2
        else:
            break

    # 'c'로 시작될 때 'chu'인지 확인하고
    # 맞다면 다음을 탐색하기 위해 그 글자수만큼 idx에 더해줌
    # 만약 아니라면 발음할 수 있는 문자열이 아니므로 종료
    elif S[idx] == 'c':
        if idx+2 < len(S) and S[idx+1:idx+3] == 'hu':
            idx += 3
        else:
            break

    # 'p', 'k', 'c'로 시작하지 않으면
    # 발음할 수 있는 문자열이 아니므로 종료
    else:
        break

# 도중에 종료되지 않고 끝까지 탐색되었다면
# 피카츄가 발음할 수 있는 문자열이므로
# is_pikachu를 True로 값 갱신 
else:
    is_pikachu = True

# is_pikachu 값에 따라 적절한 값을 출력
if is_pikachu:
    print('YES')
else:
    print('NO')