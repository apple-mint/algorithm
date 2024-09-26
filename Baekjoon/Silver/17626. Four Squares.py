# 17626. Four Squares
# https://www.acmicpc.net/problem/17626

import sys, math
input = sys.stdin.readline

# n이 주어졌을 때 몇 개의 제곱수로
# n을 표현할 수 있는지 확인하고 그 수를 반환하는 함수
def squares(n):

    # 만약 n이 제곱수일 경우
    # 하나의 제곱수로 n을 표현할 수 있으므로 1을 반환
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    
    # 만약 n이 제곱수가 아니라면
    # 1~n 범위 내에 있는 제곱수들을 찾아
    # n에 뺐을 때 남은 값이 제곱수인지 확인
    # 만약 그렇다면 2개의 제곱수로
    # n을 표현할 수 있으므로 2를 반환
    for n1 in range(1, int(math.sqrt(n))+1):
        if int(math.sqrt(n-n1**2)) == math.sqrt(n-n1**2):
            return 2
    
    # 위와 같은 방법으로 3개의 제곱수로
    # n을 표현할 수 있는지를 확인하고 그렇다면 3을 반환
    for n1 in range(1, int(math.sqrt(n))+1):
        for n2 in range(1, int(math.sqrt(n-n1**2))+1):
            if int(math.sqrt(n-n1**2-n2**2)) == math.sqrt(n-n1**2-n2**2):
                return 3

    # 모든 자연수는 넷 이하의 제곱수의 합으로
    # 표현할 수 있으므로 4를 반환      
    return 4


n = int(input().rstrip())

# n을 표현하는 제곱수들의 최소 개수 출력
print(squares(n))