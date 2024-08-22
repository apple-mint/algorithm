# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):

    # 주어진 던전의 개수의 범위가 1 이상 8 이하이기 때문에
    # N!일 때 최대 40,320으로 시간초과가 나지 않으므로
    # permutations를 이용하여 모든 경우의 수를 만듦
    permus = list(permutations(dungeons, len(dungeons)))
    
    # 탐험할 수 있는 최대 던전 수의 최댓값
    answer = 0

    # 만든 경우의 수를 모두 탐색
    # 하나를 탐색할 때마다 피로도 K,
    # 탐험할 수 있는 최대 던전 수 cnt 초기화
    for permu in permus:
        K = k
        cnt = 0

        # 만약 현재 피로도가 최소 필요 피로도보다
        # 높거나 같은 경우 탐험할 수 있으므로
        # K에 소모 피로도를 빼주고 cnt에 1을 더해줌
        for p in permu:
            if K >= p[0]:
                K -= p[1]
                cnt += 1
        
        # 만약 탐색을 종료했을 때 cnt가 던전의 개수라면
        # 해당 경우의 수로 모든 던전을 탐험할 수 있다는 의미이고
        # 더 탐색할 필요가 없으므로 cnt로 값 갱신 후 종료
        if cnt == len(dungeons):
            answer = cnt
            break

        # 아니라면 기존에 구한 최댓값과 cnt 중
        # 무엇이 최댓값인지 확인하고 그 값으로 갱신
        else:
            answer = max(answer, cnt)
    
    return answer