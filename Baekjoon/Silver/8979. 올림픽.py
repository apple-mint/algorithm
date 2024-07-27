# 8979. 올림픽
# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

nations = []
for _ in range(N):
    info = list(map(int, input().rstrip().split()))
    nations.append(info)

# 순위를 정하기 위해 금메달, 은메달, 동메달 순으로 내림차순 정렬
nations.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

# 등수는 자신보다 더 잘한 나라 수 + 1이므로
# rank: 등수, cnt: 자신보다 더 잘한 나라 수를 다음과 같이 설정
rank = 1
cnt = 0

# 내림차순 정렬로 1. 금메달 수가 더 많은 나라,
# 2. 금메달 수가 같을 경우 은메달 수가 더 많은 나라,
# 3. 금, 은메달 수가 모두 같으면 동메달 수가 더 많은 나라 순으로
# 정렬된 리스트를 순차적으로 탐색하며 등수가 동일한 경우를 탐색
for i in range(N):
    nation = nations[i]

    # 만약 인덱스 번호가 자연수인 경우
    # 앞선 나라가 존재한다는 의미이므로
    # 이 앞선 나라와 메달 수를 비교
    if i:
        pre_nation = nations[i-1]

        # 자신보다 앞선 나라 수에 1를 더해줌
        cnt += 1

        # 만약 금, 은, 동메달 수가 같다면
        # 등수는 앞선 나라와 동일하므로 아무런 연산을 진행하지 않음
        if nation[1] == pre_nation[1] and nation[2] == pre_nation[2] and nation[3] == pre_nation[3]:
            pass
        
        # 만약 다르다면 여태까지 기록된 자신보다 앞선 나라 수를
        # 현재 기록된 등수에 더해 등수를 갱신하고 cnt를 초기화
        else:
            rank += cnt
            cnt = 0

    # 만약 해당 국가가 몇 등인지 궁금한 나라라면
    # 더이상의 탐색을 종료하고 해당값을 출력토록 함
    if nation[0] == K:
        print(rank)
        break