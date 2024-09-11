# 2877. 4와 7
# https://www.acmicpc.net/problem/2877

import sys
input = sys.stdin.readline

# 한자리수 (1~2번째 작은 수)    # 두자리수 (3~6번째 작은 수)
# 0   1                       # 0   1   2   3
# 0   1                       # 00 01 10 11
# 4   7                       # 44 47 74 77

# 세자리수 (7~14번째 작은 수)
# 0    1    2   3   4   5   6   7
# 000 001 010 011 100 101 110 111
# 444 447 474 477 744 747 774 777

# 이진수로 표현할 경우 위와 같은 규칙을 찾을 수 있으므로
# 이를 활용해 4와 7로만 이루어진 수를 구할 것

K = int(input().rstrip())

# n: 자릿수
n = 1

# start: 해당 자릿수의 시작
start = 1

# end: 해당 자릿수의 끝
end = 2

while True:

    # K번째가 범위 내에 속할 경우 종료
    if start <= K <= end:
        break
    
    # 그렇지 않다면 자릿수에 1을 더해주고
    # 시작과 끝을 그 자릿수 다음 범위로 설정
    n += 1
    start = end+1
    end = start + 2**n-1

# 해당 범위에서 K번째가 몇 번째인지 계산 후
# 이를 이진수로 변환하고 숫자 부분의 길이 저장
len_binum = len(str(bin(K-start))[2:])

# 숫자 앞이 0일 경우 이진수로 변환 시 표현되지 않으므로
# 전체 자릿수에서 이진수로 변환한 숫자 부분의 길이를 빼 더해줌
bin_num = '0'*(n-len_binum) + str(bin(K-start))[2:]

# 0을 4, 1을 7로 변환해
# 창영이가 좋아하는 숫자 중 K번째 작은 수를 출력
num = ''
for b in bin_num:
    if b == '0':
        num += '4'
    else:
        num += '7'

print(num)