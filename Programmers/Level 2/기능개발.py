# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):

    # popleft 메서드 사용 위해 deque로 변환
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []

    # 모든 기능이 개발되어 배포할 때까지 반복
    while progresses:
        cnt = 0

        # 하루에 각 기능의 개발속도에 따라
        # 얼마나 개발이 진행되었는지를 계산
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 만약 배포할 기능이 남아 있고
        # 첫번째 기능이 배포할 수 있는 상태라면
        # cnt에 1를 더해주고 완료된 기능과 해당 기능의 개발속도 제거
        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        
        # 만약 배포할 기능이 있다면 그 수를 삽입
        if cnt:
            answer.append(cnt)
    
    return answer