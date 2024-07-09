# 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/?envType=daily-question&envId=2024-07-09

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        cur_time = 0
        wait_time = 0

        for customer in customers:
            arr_time, pre_time = customer

            # 손님이 준비하는 시간 도중에 도착했는지 아니면
            # 준비가 다 끝나고 바로 준비할 수 있는 시간에 도착했는지 계산
            cur_time = max(arr_time, cur_time)

            # 현재 시간에 준비하는 시간을 더하고
            # 준비를 마친 시간 - 손님이 도착한 시간을 빼 기다린 시간 계산
            cur_time += pre_time
            wait_time += cur_time - arr_time

        return wait_time / len(customers)