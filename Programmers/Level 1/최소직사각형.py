# 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    
    # 모든 명함이 만들 지갑 안에 들어가야 하므로
    # 가로 길이, 세로 길이의 최댓값을 구하면 됨
    max_w, max_h = 0, 0
    
    # 직사각형 형태의 명함을
    # 가로가 긴 모양으로 통일시켜 비교
    for w, h in sizes:

        # 만약 세로가 더 길다면 명함 회전
        if w < h:
            w, h = h, w

        if w > max_w:
            max_w = w
        
        if h > max_h:
            max_h = h
    
    # 구한 최댓값으로 지갑의 크기를 구하고 반환
    answer = max_w * max_h
    
    return answer