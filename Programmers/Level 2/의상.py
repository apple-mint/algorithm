# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):

    # 2024년 7월 30일 푼 문제와 동일한 유형
    # 9375. 패션왕 신해빈(https://www.acmicpc.net/problem/9375)

    # 한 종류에 의상이 몇 개 있는지를 기록
    # defaultdict 사용해 key가 없는 경우는 0으로 초기값 설정
    kind = defaultdict(int)
    for _, cnt in clothes:
        kind[cnt] += 1
    
    # 한 의상 종류에서 나올 수 있는 경우의 수는 
    # 해당 종류의 의상 수 + 아무것도 선택하지 않는 경우이고
    # 이는 동시에 일어나는 일이므로 해당 값을 곱해줌
    answer = 1
    for cnt in kind.values():
        answer *= (cnt+1)

    # 모든 의상을 고르지 않는 경우를
    # 제외하기 위해 1를 빼줌
    answer -= 1
    
    return answer