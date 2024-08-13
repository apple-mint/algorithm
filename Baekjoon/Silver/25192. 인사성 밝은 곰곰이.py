# 25192. 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192

import sys
input = sys.stdin.readline

N = int(input().rstrip())

cnt = 0
users = {}
for _ in range(N):
    chat = input().rstrip()

    # 새로운 사람이 채팅방에 입장했다면
    # 여태까지 채팅을 입력한 유저 닉네임 목록 초기화
    if chat == 'ENTER':
        users = {}

    else:
        # 새로운 사람의 입장이 아닐 경우
        # 채팅을 입력한 유저가 새로운 사람이 들어오고 나서
        # 처음 채팅을 입력했는지 확인
        if not users.get(chat):

            # 만약 그렇다면 곰곰티콘으로 인사한 것이므로
            # users에 해당 유저의 닉네임을 저장하고 cnt에 1를 더해줌
            users[chat] = 1
            cnt += 1

print(cnt)