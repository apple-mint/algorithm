# 1436. 영화감독 숌
# https://www.acmicpc.net/problem/1436

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# num: 자연수
# cnt: 6이 적어도 3개 이상 연속으로 들어가는 순서
num = 0
cnt = 0

# cnt가 찾는 N번째와 일치할 때까지 자연수 탐색
while cnt != N:
    num += 1
    
    # 666이 들어있는지 아닌지를 확인하기 위해
    # 문자열로 형변환하여 확인 후 맞다면 cnt에 1을 더해줌
    if '666' in str(num):
        cnt += 1

# N번째에 해당하는 수 출력
print(num)