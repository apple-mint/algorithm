# 10814. 나이순 정렬
# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for i in range(N):
    age, name = input().rstrip().split()
    age = int(age)

    # 1. 나이가 증가하는 순으로,
    # 2. 나이가 같으면 먼저 가입한 사람순으로
    # 오름차순을 하기 위해 나이, 몇 번째로 가입을 했는지,
    # 회원의 이름 순으로 arr에 삽입
    arr.append((age, i, name))

# 나이, 가입순서를 기준으로 오름차순 정렬
arr.sort()

# 나이, 이름을 공백으로 구분해 출력
for i in range(N):
    print(arr[i][0], arr[i][2])