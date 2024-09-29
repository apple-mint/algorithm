# 2503. 숫자 야구
# https://www.acmicpc.net/problem/2503

import sys, collections, itertools
input = sys.stdin.readline

N = int(input().rstrip())

nums = collections.defaultdict(int)

# 각 자릿수를 하나하나 탐색하므로
# 인덱스로 접근하기 위해 타입이 문자열인 숫자 목록을 만듦
str_nums = ['1','2','3','4','5','6','7','8','9']

# 서로 다른 숫자 세 개로 구성된
# 세 자리 수를 만들기 위해 순열 사용
permus = list(itertools.permutations(str_nums, 3))

for _ in range(N):
    num, strike, ball = map(int, input().rstrip().split())

    # 자릿수 비교를 위해 문자열로 형변환
    num = str(num)
    
    # 민혁이 말한 숫자와 순열들을 비교하며
    # 동일한 자리에 위치하면 스트라이크로,
    # 다른 자리에 위치하면 볼 1번으로 세 더해줌
    for permu in permus:
        s, b = 0, 0
        
        for i in range(3):
            for j in range(3):
                if num[i] == permu[j]:
                    if i == j:
                        s += 1
                    else:
                        b += 1

        # 만약 영수가 답한 스트라이크 개수,
        # 볼의 개수와 그 수들이 일치한다면
        # 영수가 생각하고 있을 가능성이 있는 답일 수 있으므로
        # 비교한 순열을 세 자리 수 형태로 만들어주고
        # 해당 값을 key으로 가지는 value에 1을 더해줌 
        if s == strike and b == ball:
            permu = permu[0] + permu[1] + permu[2]
            nums[permu] += 1

cnt = 0

# 영수가 생각하고 있을 가능성이 있는 수라면
# 질문을 한 횟수만큼 영수가 답한 스트라이크 개수,
# 볼의 개수와 그 수들이 일치한다고 나왔을 것이므로
# value가 N과 같은 것이 몇 개 있는지를 확인
for num in nums.keys():
    if nums[num] == N:
        cnt += 1

# 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력
print(cnt)