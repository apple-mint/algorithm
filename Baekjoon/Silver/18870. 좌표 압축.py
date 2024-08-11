# 18870. 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

# 정렬 후에도 입력받은 좌표값의 순서를
# 파악할 수 있도록 인덱스를 추가해 저장
for i in range(N):
    arr[i] = (arr[i], i)

# 좌표값을 기준으로 오름차순 정렬
arr.sort()

num = 0
ans = {}
for i in range(N):
    idx = arr[i][1]

    # 이전에 비교할 좌표값이 있으면 현재 좌표값과 비교
    # 만약 다르다면 num에 1을 더해
    # 이전 값보다 다음에 좌표가 있음을 표현
    if i:
        if arr[i][0] != arr[i-1][0]:
            num += 1
    
    # 해당 인덱스를 key로,
    # 좌표 순서를 value로 ans에 저장
    ans[idx] = num

# 공백 한 칸으로 구분해서 출력
for idx in range(N):
    print(ans[idx], end=' ')