# 5635. 생일
# https://www.acmicpc.net/problem/5635

import sys
input = sys.stdin.readline

n = int(input().rstrip())

students = []
for _ in range(n):
    name, d, m, y = input().rstrip().split()
    d, m, y = int(d), int(m), int(y)
    students.append((y, m, d, name))

# 연도, 월, 일 순으로 오름차순해
# 가장 나이가 많은 사람이 첫번째가 되도록 정렬
students.sort()

# 가장 나이가 적은 사람의 이름,
# 가장 나이가 많은 사람의 이름을 출력
print(students[-1][-1])
print(students[0][-1])