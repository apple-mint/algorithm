# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        ans = answers[i]
        
        # 각자 찍는 방식에 따라 인덱스가 반복될 수 있도록
        # 그 길이만큼 나눴을 때의 나머지로 값을 찾을 수 있게 하고
        # 만약 그 값이 정답과 같다면 cnt에 1을 더해줌
        if a1[i%5] == ans:
            cnt1 += 1
        if a2[i%8] == ans:
            cnt2 += 1
        if a3[i%10] == ans:
            cnt3 += 1
    
    # 가장 많은 문제를 맞힌 사람이 누구인지 알기 위해
    # 맞은 문제의 최댓값을 구함
    maxx = max(cnt1, cnt2, cnt3)

    # 만약 가장 높은 점수를 받은 사람이 여럿일 경우
    # 오름차순으로 나타내기 위해 1부터 순차적으로 삽입
    if cnt1 == maxx:
        answer.append(1)
    if cnt2 == maxx:
        answer.append(2)
    if cnt3 == maxx:
        answer.append(3)
    
    return answer