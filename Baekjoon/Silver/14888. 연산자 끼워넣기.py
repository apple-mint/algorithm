# 14888. 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline

# 하나의 경우의 수를
# 끝까지 탐색해야 하므로 dfs 구현 
def dfs(num, cnt):
    global maxx, minn

    # 주어진 연산자를 모두 사용했다면
    # 만들어진 식의 결과가
    # 최대인지 최소인지 확인하고 종료
    if cnt == N-1:
        maxx = max(maxx, num)
        minn = min(minn, num)
        return
    
    for i in range(4):

        # 만약 해당 연산자를 쓸 수 있다면
        # 해당 연산자에 맞는 계산 진행
        if operators[i]:

            # cnt에 1을 더하고
            # 해당 연산자에 해당하는 값에 1을 빼줌
            cnt += 1
            operators[i] -= 1

            # 문제에 나와있는 방법에 따라 계산하고
            # 그 결과를 dfs 함수에 넣어 다시 함수를 호출해
            # 연산자를 모두 사용해 식을 만들 수 있도록 함
            if i == 0:
                dfs(num+A[cnt], cnt)
            elif i == 1:
                dfs(num-A[cnt], cnt)
            elif i == 2:
                dfs(num*A[cnt], cnt)
            else:
                if num >= 0:
                    dfs(num//A[cnt], cnt)
                else:
                    dfs(-(abs(num)//A[cnt]), cnt)

            # 다른 방식으로 식을 만들기 위해
            # 해당 경우의 수의 계산을 끝냈다면
            # 그 이전으로 해당 값들을 되돌림
            cnt -= 1
            operators[i] += 1


N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
operators = list(map(int, input().rstrip().split()))

# 만들 수 있는 식의 결과의
# 최대와 최소의 초기값 설정 후
# dfs 함수 호출을 통해 해당 값들을 계산
maxx = float('-inf')
minn = float('inf')
dfs(A[0], 0)

# 만들 수 있는 식의 결과의
# 최댓값과 최솟값을 출력
print(maxx)
print(minn)