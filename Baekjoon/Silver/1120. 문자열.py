# 1120. 문자열
# https://www.acmicpc.net/problem/1120

import sys
input = sys.stdin.readline

A, B = input().rstrip().split()

# A와 B의 길이가 같다면
# A의 앞 혹은 뒤에 아무 알파벳이나
# 추가하는 연산이 불필요하므로 A와 B의 차이를 계산
if len(A) == len(B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1

# 만약 아니라면 A의 전체가 B의 부분과
# 가장 많이 일치하는 구간을 찾고 그 위치를 기준으로
# 그 앞 혹은 뒤에 B의 해당 위치에 있는 알파벳을 추가한다면
# A와 B의 차이를 최소가 되도록 할 수 있으므로
# 다음과 같은 구간을 찾아 A와 B의 차이를 계산
else:

    # A와 B의 길이는 최대 50이므로
    # 될 수 있는 최댓값 49에 1을 더해 초기값 설정
    cnt = 50

    # A 전체를 B가 시작하는 지점부터
    # 하나하나 맞춰보면서 A와 B의 차이를 계산
    for i in range(len(B)-len(A)+1):

        # 해당 구간의 A와 B의 차이
        minn = 0
        
        for j in range(len(A)):
            if A[j] != B[i+j]:
                minn += 1

        # 가장 많이 일치하는 구간인지 최솟값 비교 후
        # 현재 구한 값이 최솟값이면 값 갱신
        cnt = min(cnt, minn)

print(cnt)