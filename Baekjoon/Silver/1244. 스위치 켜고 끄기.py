# 1244. 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline

N = int(input().rstrip())
switch = list(map(int, input().rstrip().split()))
student = int(input().rstrip())

for _ in range(student):
    gender, num = map(int, input().rstrip().split())

    # 성별이 남자일 경우 주어진 수의 배수에 해당하는
    # 스위치 번호를 바꾸는 것이므로 나누어떨어질 때 조작
    if gender == 1:
        for i in range(N):

            # 인덱스 번호가 0부터 시작하므로 1을 더해줌
            if not (i+1) % num:
                if switch[i]:
                    switch[i] = 0
                else:
                    switch[i] = 1
    
    else:
        # 인덱스 번호가 0부터 시작하므로 편의를 위해 1을 빼줌
        num -= 1

        # 가장 많은 스위치를 포함하는 구간을 찾아 바꾸는 것이므로
        # 같은 번호의 스위치는 좌우 대칭 여부와 상관없이 바꿔줘야 함
        if switch[num]:
            switch[num] = 0
        else:
            switch[num] = 1

        # 좌우가 대칭인지 확인
        # 스위치 번호가 범위 내에 있으며 좌우가 대칭일 경우 조작
        for j in range(1, N):
            if 0<=num+j<N and 0<=num-j<N and switch[num+j] == switch[num-j]:
                if switch[num+j]:
                    switch[num+j], switch[num-j] = 0, 0
                else:
                    switch[num+j], switch[num-j] = 1, 1

            # 그렇지 않다면 좌우가 대칭인 구간이 끝났으므로 종료
            else:
                break

for idx in range(N):

    # 한 줄에 20개씩 출력하므로 나머지는 빈칸을 두고
    # 스위치 번호가 20으로 나누어떨어질 경우에만 줄바꿈
    if (idx+1) % 20:
        print(switch[idx], end=' ')
    else:
        print(switch[idx])