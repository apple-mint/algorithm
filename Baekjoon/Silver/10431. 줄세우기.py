# 10431. 줄세우기
# https://www.acmicpc.net/problem/10431

import sys
input = sys.stdin.readline

P = int(input().rstrip())
for _ in range(P):
    nums = list(map(int, input().rstrip().split()))
    T = nums[0]
    children = nums[1:]

    cnt = 0
    for i in range(20):

        # 앞에 서 있는 학생이 있을 때
        # 앞에 있는 모든 학생들보다 큰지 비교
        if i:

            # 인덱스가 변할 수 있으므로
            # 기준 학생의 키를 저장
            student = children[i]

            # 앞에 있는 모든 학생들보다 키가 큰지 비교
            # 만약 키가 큰 학생이 있다면
            # 그 학생과의 거리 차를 구해 cnt에 더하고
            # 그 학생 앞으로 위치를 이동하고
            # 다음 학생들의 키를 비교하기 위해 종료
            for j in range(i):
                if student < children[j]:
                    children.remove(student)
                    cnt += i-j
                    children.insert(j, student)
                    break

    # 출력 예시에 따라 결과를 출력
    print(T, cnt)