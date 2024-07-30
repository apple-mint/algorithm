# 14713. 앵무새
# https://www.acmicpc.net/problem/14713

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

parrots = {}
len_S = 0
for i in range(N):

    # 앵무새가 말하는 동안 다른 앵무새가 도중에 말을 가로채
    # 다른 문장의 단어를 말할 수 있으므로 용이한 비교를 위해
    # popleft, appendleft 메서드가 있는 deque 활용
    parrots[i] = collections.deque(input().rstrip().split())

    # 앵무새에게 말한 단어들의 수를 기록
    len_S += len(parrots[i])

L = input().rstrip().split()

cnt = 0
for j in range(len(L)):

    # 받아 적은 문장의 단어 하나하나를 기준점으로 정함
    standard = L[j]

    # 앵무새 N마리가 말한 문장들의 첫 단어를 탐색
    for k in range(N):
        if parrots[k]:
            word = parrots[k].popleft()

            # 만약 받아 적은 문장의 단어와 일치한다면
            # 일치한다는 의미로 cnt에 1를 더해줌
            if word == standard:
                cnt += 1
                break
            
            # 만약 일치하지 않는다면 제자리로 복구
            else:
                parrots[k].appendleft(word)

# 문제에는 언급되지 않았으나
# 앵무새가 말한 문장 그대로가 전달되어야 하므로
# 1. 앵무새가 말한 단어들의 수,
# 2. 받아 적은 단어들의 수,
# 3. 규칙에 따라 탐색했을 때 일치한 단어들의 수를 기록한 cnt
# 위 세 가지 경우의 수가 모두 일치해야 가능한 문장이 될 수 있음
if cnt == len(L) == len_S:
    print('Possible')

# 그렇지 않을 경우 불가능한 문장
else:
    print('Impossible')