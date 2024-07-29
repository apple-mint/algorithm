# 1316. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

for _ in range(N):
    word = input().rstrip()

    # 단어의 어떤 문자가 나왔는지 확인하기 위한 딕셔너리
    alphabet = {}

    # 인덱스 번호를 0으로 시작하고
    # while문으로 word 마지막 문자까지 탐색
    idx = 0
    while idx < len(word):

        a = word[idx]

        # 만약 해당 문자가 처음으로 나온 문자라면
        # alphabet에 나왔다는 표시로 1로 값을 변경
        if not alphabet.get(a):
            alphabet[a] = 1

            # 그 문자가 어디까지 연속해서 나오는지를 확인하고자
            # 단어 범위 내에서 그 다음 문자가 해당 문자와 같다면
            # 그 다음으로 계속 이동
            while idx+1 < len(word) and word[idx+1] == a:
                idx += 1

        # 만약 해당 문자가 나온 적이 있다면
        # 연속해서 나타나는 경우가 아니므로 탐색 종료
        else:
            break
        
        # 하나의 문자 탐색이 끝났다면
        # 다음 문자를 탐색하고자 idx에 1을 더해줌
        idx += 1
    
    # 만약 도중에 while문이 멈춰지지 않았다면
    # 그룹 단어라는 의미이므로 cnt에 1을 더해줌
    else:
        cnt += 1

# 그룹 단어의 개수 출력
print(cnt)