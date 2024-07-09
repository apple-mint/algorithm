# 2582. Pass the Pillow
# https://leetcode.com/problems/pass-the-pillow/description/?envType=daily-question&envId=2024-07-06

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        # 문제에서 n과 time의 값이 1000 이하이므로
        # 하나하나 확인하면서 계산

        # num: 시작점, move: 움직이는 방향
        num = 1
        move = 1
        
        # 주어진 시간만큼 이동
        for t in range(1, time+1):
            num += move

            # 끝까지 도달했을 경우 방향을 바꿔 돌아오고
            # 1초당 1칸씩 이동하므로 나눠 떨어질 때 방향 전환
            if not t % (n-1):
                move *= (-1)

        return num