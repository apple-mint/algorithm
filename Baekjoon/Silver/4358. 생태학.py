# 4358. 생태학
# https://www.acmicpc.net/problem/4358

import sys
input = sys.stdin.readline

cnt = 0
tree = {}

# 입력이 몇번인지 구체적으로 나와 있지 않으므로
# 입력값이 없을 경우 종료되도록 작성
while True:
    name = input().rstrip()

    if not name:
        break
    
    else:
        # 입력값이 총 얼마인지 구하기 위해 cnt에 1을 더함
        cnt += 1

        # 만약 먼저 나온 종 이름일 경우
        # 기존에 있던 값에 1을 더해 갱신
        if tree.get(name):
            tree[name] += 1
        
        # 처음 나온 종 이름일 경우
        # 새롭게 값을 만들어 1를 표기
        else:
            tree[name] = 1

# 각 종의 이름을 사전순으로 출력하기 위해 키값을 기준으로 정렬
for k, v in sorted(tree.items()):

    # round 함수의 경우 오사오입으로
    # 흔히 아는 사사오입 구현 위해 0.00001을 더함
    rate = round((v / cnt * 100) + 0.00001, 4)

    # 소수점 4째자리까지 출력하기 위해 f-string 사용
    print(f'{k} {rate:.4f}')