# 12933. 오리
# https://www.acmicpc.net/problem/12933

import sys
input = sys.stdin.readline

sound = input().rstrip()

# 한 오리당 내는 소리를 구분하기 위해
# 리스트를 하나의 요소로 가지도록 설정
ducks = [[]]

# 녹음한 소리가 올바른지 아닌지
# 확인하는 변수의 초기값을 False로 설정
is_valid = False

# 녹음한 소리를 확인
for i in range(len(sound)):

    # 녹음한 소리가 'q'일 경우
    if sound[i] == 'q':

        # 만약 이전에 어떤 오리가 'quack'으로 울어
        # 빈 리스트가 있거나 첫 녹음소리라 초기값 상태인 경우
        # 해당 빈 리스트에 'q'를 삽입하고 종료해 다음으로 이동
        for j in range(len(ducks)):
            if not ducks[j]:
                ducks[j].append(sound[i])
                break

        # 아니라면 모든 오리의 울음 소리가 끝나지 않았으므로
        # 'q'가 담긴 리스트를 새로 만들어 삽입
        else:
            ducks.append([sound[i]])
    
    # 녹음한 소리가 'u'일 경우
    elif sound[i] == 'u':

        # 'u'의 앞에는 반드시 'q'가 있어야 하므로
        # 마지막이 'q'인 리스트를 찾아
        # 해당 리스트에 'u'를 삽입하고 종료해 다음으로 이동
        for duck in ducks:
            if duck and duck[-1] == 'q':
                duck.append(sound[i])
                break
        
        # 만약 없다면 올바르지 않으므로
        # 녹음한 소리를 확인하는 것을 종료
        else:
            break

    # 녹음한 소리가 'a'일 경우
    elif sound[i] == 'a':

        # 'a'의 앞에는 반드시 'u'가 있어야 하므로
        # 마지막이 'u'인 리스트를 찾아
        # 해당 리스트에 'a'를 삽입하고 종료해 다음으로 이동
        for duck in ducks:
            if duck and duck[-1] == 'u':
                duck.append(sound[i])
                break
            
        # 만약 없다면 올바르지 않으므로
        # 녹음한 소리를 확인하는 것을 종료
        else:
            break

    # 녹음한 소리가 'c'인 경우
    elif sound[i] == 'c':

        # 'c'의 앞에는 반드시 'a'가 있어야 하므로
        # 마지막이 'a'인 리스트를 찾아
        # 해당 리스트에 'c'를 삽입하고 종료해 다음으로 이동        
        for duck in ducks:
            if duck and duck[-1] == 'a':
                duck.append(sound[i])
                break

        # 만약 없다면 올바르지 않으므로
        # 녹음한 소리를 확인하는 것을 종료
        else:
            break
    
    # 녹음한 소리가 'k'인 경우
    elif sound[i] == 'k':

        # 'k'의 앞에는 반드시 'c'가 있어야 하므로
        # 마지막이 'c'인 리스트를 찾고 만약 있다면
        # 'quack'로 하나의 울음 소리가 끝났기 때문에
        # 해당 리스트를 초기화하고 종료해 다음으로 이동
        for j in range(len(ducks)):
            if ducks[j] and ducks[j][-1] == 'c':
                ducks[j] = []
                break

        # 만약 없다면 올바르지 않으므로
        # 녹음한 소리를 확인하는 것을 종료
        else:
            break

# 만약 소리를 전부 확인했다면
# 각 오리가 quack으로 울었는지 확인
else:

    # 각 오리별로 남은 녹음한 소리가 있는지 확인
    for duck in ducks:

        # 만약 있다면 끝까지 울지 못한 것이고
        # 올바르지 않으므로 종료
        if duck:
            break

    # 전부 없다면 올바르게 녹음한 것이므로
    # is_valid의 값을 True로 갱신
    else:
        is_valid = True

# 만약 올바르게 녹음한 소리라면
# ducks의 요소의 개수를 세 출력
if is_valid:
    print(len(ducks))

# 아니라면 -1 출력
else:
    print(-1)