# 21608. 상어 초등학교
# https://www.acmicpc.net/problem/21608

import sys, collections
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input().rstrip())

classroom = [[0]*N for _ in range(N)]
students = {}
like = {}

for _ in range(N**2):
    student, num1, num2, num3, num4 = map(int, input().rstrip().split())

    # 한 학생이 어떤 4명의 학생을 좋아하는지
    # 학생 번호를 key값으로 like에 저장
    like[student] = (num1, num2, num3, num4)

    # 해당 학생이 앉을 수 있는 칸의 후보
    candidate = collections.defaultdict(int)

    # 해당 학생이 좋아하는 4명의 학생들과
    # 인접한 칸에 앉지 못해 다른 빈자리를
    # 찾아야 하는지 확인하는 변수
    flag = True
    for num in like[student]:

        # 규칙 1에 따라 비어있는 칸 중 좋아하는 학생이
        # 인접한 칸에 가장 많은 칸에 앉을 수 있도록
        # 좋아하는 학생이 자리에 앉았는지 확인
        if students.get(num):
            r, c = students.get(num)

            # 좋아하는 학생의 인접한 칸 중
            # 빈 칸이 있다면 flag를 False로 바꾸고
            # 해당 좌표를 key로 가지고 있는 value에 1를 더해줌
            for d in delta:
                nr, nc = r+d[0], c+d[1]
                if 0<=nr<N and 0<=nc<N and not classroom[nr][nc]:
                    flag = False
                    candidate[(nr,nc)] += 1

    # 만약 좋아하는 4명의 학생들보다 먼저 칸에 앉거나
    # 좋아하는 4명의 학생들의 인접한 칸이 빈 칸이 아닐 경우
    # 빈 칸을 찾아 해당 좌표를 key로 가지고 있는 value에 1를 더해줌
    if flag:
        for r in range(N):
            for c in range(N):
                if not classroom[r][c]:
                    candidate[(r,c)] += 1

    # 규칙 2에 따라 규칙 1을 만족하는 칸이 여러 개일 경우
    # 인접한 칸 중 비어있는 칸이
    # 가장 많은 칸에 앉을 수 있도록
    # 가장 많이 후보로 선발된 칸이 무엇인지 구함
    maxx = max(candidate.values())

    for candi in candidate.keys():

        # 가장 많이 후보로 선발된 칸의
        # 인접한 칸이 비어있다면
        # 해당 좌표를 key로 가지고 있는 value에 1를 더해줌
        if candidate[candi] == maxx:
            for d in delta:
                nr = candi[0] + d[0]
                nc = candi[1] + d[1]
                
                if 0<=nr<N and 0<=nc<N and not classroom[nr][nc]:
                    candidate[candi] += 1

    # 규칙 3에 따라 규칙 2를 만족하는 칸이 여러 개일 경우
    # 행의 번호, 열의 번호 순으로 가장 작은 칸에 앉을 수 있도록 
    # 가장 많이 후보로 선발된 칸이 무엇인지 구함
    maxx = max(candidate.values())

    # 번호 순서가 중요하므로 후보 좌표들을
    # 오름차순으로 정렬 후 탐색
    for candi in sorted(candidate.keys()):

        # 가장 많이 후보로 선발된 칸이 나왔다면
        # 해당 칸에 학생을 앉게 하고
        # 교실에 앉아 있다는 표시를 해준 뒤 탐색 종료
        if candidate[candi] == maxx:
            r, c = candi
            classroom[r][c] = student
            students[student] = (r, c)
            break

ans = 0

# 자리 배치가 모두 끝난 후 만족도를 구함
for r in range(N):
    for c in range(N):
        cnt = 0
        num = classroom[r][c]

        # 해당 학생의 인접한 칸에
        # 좋아하는 학생이 몇 명 있는지 탐색
        for d in delta:
            nr, nc = r+d[0], c+d[1]
            if 0<=nr<N and 0<=nc<N and classroom[nr][nc] in like[num]:
                cnt += 1

        # 학생의 수에 따른 만족도를 계산
        if cnt:
            ans += 10**(cnt-1)

# 학생의 만족도의 총합 출력
print(ans)