# 1550. Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/submissions/1307103353/?envType=daily-question&envId=2024-07-01

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        # 연속으로 홀수가 있는지 확인
        cnt = 0

        for num in arr:

            # 만약 홀수일 때 하나를 더해줌
            if num % 2:
                cnt += 1

            # 짝수이면 홀수가 연속되지 않으므로 초기화
            else:
                cnt = 0

            # 홀수가 연속되어 3개가 나올 경우 참이므로 True
            if cnt == 3:
                return True

        # 끝까지 살펴봤는데도 없다면 False
        return False
        