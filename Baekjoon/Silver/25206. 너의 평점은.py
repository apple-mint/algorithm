# 25206. 너의 평점은
# https://www.acmicpc.net/problem/25206

import sys
input = sys.stdin.readline

score = {
    'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0
}

cnt = 0
answer = 0
for _ in range(20):
    name, credit, grade = input().rstrip().split()
    credit = float(credit)

    # 등급이 P인 과목은 계산에서 제외하고
    # 나머지 등급으로 등급에 따른 점수를 구함
    # 학점의 총합으로 나누기 위해 cnt에 학점을 더해주고
    # score를 참고해 answer에 (학점x과목평점)을 구해 더해줌
    if grade != 'P':
        cnt += credit
        answer += credit * score[grade]

# 위에서 구한 값을 바탕으로
# 전공평점을 계산해 출력
print(answer/cnt)