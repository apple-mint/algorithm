# 10773. 제로
# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

K = int(input().rstrip())

# 가장 최근에 나온 수를 쉽게 제거하고자
# pop 메서드를 사용할 수 있는 리스트 형태로 지정
money = []
for _ in range(K):
    num = int(input().rstrip())

    # 주어진 정수가 0일 경우 가장 최근에 쓴 수를 제거
    if not num:
        money.pop()

    # 만약 0이 아닌 정수일 경우 money에 삽입
    else:
        money.append(num)

# 최종적으로 남아 있는 수들의 합을 출력
print(sum(money))