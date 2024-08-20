# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0

    # 구명보트에 최대 2명씩 타야 한다면
    # 가장 무거운 사람 + 가장 가벼운 사람 조합이
    # 구명보트를 최대한 적게 사용할 수 있음

    # 가장 가벼운 사람을 가리키는 인덱스
    left = 0

    # 가장 무거운 사람을 가리키는 인덱스
    right = len(people)

    # 사람들의 몸무게를 오름차순 정렬
    people.sort()

    # 가장 가벼운 사람 + 가장 무거운 사람 조합이
    # 가능한지 투 포인터 알고리즘으로 탐색
    while left < right:

        # right의 초기값이 배열의 길이이므로
        # 인덱스 번호를 맞추기 위해 시작 전 1을 빼줘
        # 가장 무거운 사람의 몸무게를 찾을 수 있도록 함
        right -= 1

        # 만약 가장 가벼운 사람과 가장 무거운 사람의 합이
        # 구명보트의 무게 제한 이하인 경우
        # 2명이 탈 수 있으므로 left에 1을 더해
        # 다음 가장 가벼운 사람의 몸무게를 찾을 수 있도록 함
        if people[left] + people[right] <= limit:
            left += 1
        
        # 최소 한 명 이상 구명보트에 탔으므로
        # 구명보트에 탄 명수와 상관없이 1을 더해줌
        answer += 1
    
    return answer