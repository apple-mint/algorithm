# 5525. IOIOI
# https://www.acmicpc.net/problem/5525

import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

idx = 0
cnt = 0

# 문자열 Pn이 몇 군데 포함되어 있는지를 확인하기 위해
# 해당 길이만큼 잘라 문자열 S 범위를 탐색
while idx+2*N-1 < M:

    # 만약 문자열 Pn이 포함되어 있는 경우
    # cnt에 1을 더하고 해당 문자열의 다음 인덱스로 이동
    if S[idx:idx+2*N+1] == 'I'+'OI'*N:
        cnt += 1
        idx = idx+2*N+1
        
        # 문자열 Pn 뒤에 'OI'가 몇 번 반복되는지를 확인해
        # 문자열 Pn의 개수를 세 더해줌
        while idx+1 < M and S[idx:idx+2] == 'OI':
            cnt += 1
            idx += 2
    
    # 만약 문자열 Pn이 아닐 경우
    # 다음 인덱스로 이동해 탐색할 수 있도록 함
    else:
        idx += 1

print(cnt)