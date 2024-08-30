# 18110. solved.ac
# https://www.acmicpc.net/problem/18110

import sys
input = sys.stdin.readline

n = int(input().rstrip())

opinions = []
for _ in range(n):
    opinion = int(input().rstrip())
    opinions.append(opinion)

# 의견이 없다면 난이도는 0이므로 0 출력
if not opinions:
    print(0)

# 의견이 있다면 난이도를 결정하는 방식에 따라 계산
else:

    # 가장 큰 값들과 가장 작은 값들을
    # 제외하기 위해 의견들을 오름차순 정렬
    opinions.sort()

    # 위에서 15%, 아래에서 15%에 해당하는
    # 명수를 반올림해 계산
    num = round(n*0.15+(1e-10))

    # 해당 명수를 제외하고 평균을 구하기 위한 합계 계산
    summ = sum(opinions[num:n-num])

    # 합계를 해당 명수를 제외한 값으로 나눠
    # 평균을 구하고 그 값을 정수로 반올림해 출력
    print(round(summ/(n-2*num)+(1e-10)))