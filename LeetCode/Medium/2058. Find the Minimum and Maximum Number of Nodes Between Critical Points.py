# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/?envType=daily-question&envId=2024-07-05

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minn = float('inf')

        # 최솟값, 최댓값을 구하기 위해서는 3개가 비교되어야 하므로
        # one, two, three로 변수 지정
        one = head
        two = one.next
        three = two.next

        # 최솟값 또는 최댓값이 될 가능성이 있는 위치
        two_idx = 2

        # 최솟값 또는 최댓값 사이의 거리가 최소가 되려면
        # 각 값 사이의 차가 각각 얼마인지 확인해야 함
        pre_idx = 0

        # 최솟값 또는 최댓값 사이의 거리가 최대가 되려면
        # 가장 처음값과 마지막에 나온 값을 비교해야 함
        first_idx = 0

        # 만약 마지막 노드에 더이상 연결된 노드가 없다면
        # 비교가 끝난 것이므로 종료
        while three != None:

            # 최솟값과 최댓값을 따로 구분하지 않으므로 한꺼번에 계산
            if (two.val < one.val and two.val < three.val) or (two.val > one.val and two.val > three.val):
                
                # 처음 나온 최솟값 혹은 최댓값이므로 해당 값을 저장
                if not pre_idx:
                    first_idx = two_idx

                # 이전값이 있다면 둘의 차가 최소인지 확인
                else:
                    if two_idx - pre_idx < minn:
                        minn = two_idx - pre_idx
                
                # 최솟값 또는 최댓값을 하나 발견했으므로
                # 이전값을 현재 찾은 값으로 갱신
                pre_idx = two_idx

            # 3개의 노드를 다 비교했으므로 다음 3개 탐색을 위해 이동
            one = two
            two = one.next
            three = two.next

            two_idx += 1

        # 만약 초기 최솟값이 변하지 않았을 경우
        # 최솟값 또는 최댓값이 없거나 하나라는 의미이므로 [-1, -1] 반환
        if minn == float('inf'):
            return [-1, -1]
        
        # 그게 아니라면 최댓값 계산 후 반환
        else:
            maxx = pre_idx - first_idx
            return [minn, maxx]