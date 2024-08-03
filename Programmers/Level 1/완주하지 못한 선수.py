# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    
    # 마라톤에 참가한 선수들의 명수를 기록
    # 동명이인이 있는 경우를 고려하여
    # 이름을 키값으로 나오는 수만큼 더해줌
    dit = {}
    for name in participant:
        if not dit.get(name):
            dit[name] = 1
        else:
            dit[name] += 1
    
    # 마라톤에 참가한 선수들의 명수에서
    # 완주한 선수들의 명수를 빼줌으로써 완주했는지를 기록
    for name in completion:
        dit[name] -= 1

    # 명수를 기록한 dit를 탐색했을 때
    # 만약 명수가 남아있다면 완주하지 못한 선수이므로
    # 그 이름을 answer에 갱신하고 탐색 종료
    answer = ''
    for name in dit.keys():
        if dit[name]:
            answer = name
            break
        
    return answer