# 1518. Water Bottles
# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        # cnt: 마신 물병, drink: 다 마신 물병
        cnt = 0
        drink = 0

        # 주어진 변수의 크기가 100 이하이므로
        # 마실 수 있는 물병이 남아 있을 때까지 반복
        while numBottles:
            cnt += 1
            drink += 1
            numBottles -= 1

            # 만약 마신 물병의 수가 바꿀 수 있는 물병의 수와 같아질 때
            # 마실 수 있는 물병 하나와 다 마신 물병과 교환
            if drink == numExchange:
                drink = 0
                numBottles += 1

        return cnt