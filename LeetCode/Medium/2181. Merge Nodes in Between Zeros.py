# 2181. Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-07-04

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 시작과 끝은 무조건 값이 0이므로 그 다음부터 탐색
        # ListNode 형태를 다시 만들 경우 시간초과가 나므로 기존 head를 활용
        start = head.next
        move = start

        # 노드에 연결된 값의 마지막까지 탐색
        while move:
            
            # 0과 0 사이에 있는 값의 합계
            cnt = 0

            # 0이 나오기 전까지 값을 더해주면서 이동
            while move.val:
                cnt += move.val
                move = move.next

            # 시작점에 합계를 저장
            start.val = cnt

            # 끝인 0이 나올 때까지 이동했으므로 또다른 시작점으로 이동
            move = move.next

            # start.next에 move를 참조하게 해 이미 계산한 값들 삭제
            start.next = move

            # 새로운 합계를 저장하기 위해 연결된 다음 노드로 이동
            start = start.next

        # start를 움직이며 저장했던 합계를 ListNode 형태로 반환
        return head.next