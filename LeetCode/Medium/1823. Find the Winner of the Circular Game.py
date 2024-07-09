# 1823. Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08

# 원형 큐를 사용하기 위해 import
from collections import deque 

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = deque()

        for num in range(1, n+1):
            friends.append(num)

        # 마지막 한명이 남을 때까지 반복
        while len(friends) > 1:

            # 시계방향으로 원형으로 돌아가므로
            # popleft로 꺼낸 것을 다시 append로 삽입
            for _ in range(k-1):
                friend = friends.popleft()
                friends.append(friend)

            # k번째는 탈락이므로 재삽입없이 제거
            friends.popleft()
        
        # 마지막 남은 한명 출력
        ans = friends.popleft()

        return ans