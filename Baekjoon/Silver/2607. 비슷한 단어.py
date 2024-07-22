# 2607. 비슷한 단어
# https://www.acmicpc.net/problem/2607

import sys, collections
input = sys.stdin.readline

N = int(input().rstrip())

# 기준점이 되는 입력으로 주어진 첫 번째 단어
standard = input().rstrip()
len_standard = len(standard)

# 첫 번째 단어의 철자를 파악하기 위해 딕셔너리 설정
# defaultdict를 사용하면 초기값이 자동으로 설정되므로
# 별다른 예외처리를 하지 않아도 됨
dit_standard = collections.defaultdict(int)
for i in range(len_standard):
    dit_standard[standard[i]] += 1

ans = 0

# 첫 번째 단어와 비교할 단어들을 입력받음
for _ in range(N-1):
    word = input().rstrip()
    len_word = len(word)

    dit_word = collections.defaultdict(int)
    for j in range(len_word):
        dit_word[word[j]] += 1

    # 첫 번째 단어와 그 비교할 단어에 있는
    # 철자들을 구하기 위해 합집합 연산을 함
    uni = set(standard) | set(word)

    # 비슷한 단어가 될 수 있는 조건은 다음과 같음
    # 1. 길이가 같고 나온 철자와 그 수가 모두 동일하거나,
    # 2. 길이가 같고 같은 철자의 차가 1이고 나머지는 모두 동일하거나,
    # 3. 길이가 같고 다른 철자가 있다면 그것이 서로 짝지어지거나,
    # 4. 길이가 1씩 차이가 나며 하나의 철자에서 그 차가 1이여야 함

    # 길이가 같은 경우 조건 1, 조건 2, 조건 3에 해당하는지를 탐색
    if len_standard == len_word:
        cnt = 0

        # 철자들의 합집합에서 철자 하나를 가져와 비교
        for k in uni:

            # 두 철자가 나온 수의 차를 구해
            # 그 절댓값을 더해줌
            cnt += abs(dit_standard[k] - dit_word[k])

        # 만약 cnt가 0이라면 조건 1,
        # 만약 cnt가 2라면 조건 2, 조건 3에 해당하므로 1을 더해줌
        if cnt == 0 or cnt == 2:
            ans += 1

    # 길이가 다른 경우 그 차가 1인 경우에만
    # 비슷한 단어가 될 수 있으므로 해당 경우만 탐색
    elif abs(len_standard-len_word) == 1:
        cnt = 0

        # 두 철자가 나온 수의 차를 구해
        # 그 절댓값을 더해줌
        for k in uni:
            cnt += abs(dit_standard[k] - dit_word[k])
        
        # 만약 cnt가 1이라면 조건 4에 해당하므로 1을 더해줌
        if cnt == 1:
            ans += 1

# 비슷한 단어의 개수를 출력
print(ans)