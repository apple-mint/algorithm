# 2196. Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2024-07-15

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs 구현을 위해 import
from collections import deque

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        # TreeNode 형태로 반환해야 한다는 조건에 따라 설정
        ans = TreeNode()

        # 부모 노드, 자식 노드 값이 중복돼 나오는 경우가 있으므로
        # 중복 제거를 위해 집합 사용
        parent_set = set()
        child_set = set()

        # 부모 노드가 가지고 있는 자식 노드들을
        # 빠르게 탐색하기 위해 딕셔너리 사용
        dit = {}

        # 노드 정보 탐색
        for description in descriptions:
            parent = description[0]
            child = description[1]
            is_left = description[2]

            # 나온 값들을 해당 노드에 맞춰 추가
            parent_set.add(parent)
            child_set.add(child)

            # 만약 최초로 나온 값인 경우
            # KeyError를 방지하고자 딕셔너리 값 추가
            # 최적화를 위해 필요한 값에 대해서만 딕셔너리 값 추가
            # Runtime 2751ms -> 1610ms, Memory 43.1MB -> 26.1MB로 단축
            if dit.get(parent) == None:
                dit[parent] = [0, 0]

            # 만약 왼쪽에 있는 자식 노드면 왼쪽에 추가
            if is_left:
                dit[parent][0] = child
            
            # 그렇지 않다면 오른쪽에 추가
            else:
                dit[parent][1] = child

        # 부모 노드에만 있는 값이 최상단 노드 값이므로
        # 차집합을 구한 뒤 남아 있는 값을 ans 최상단에 저장
        root = (parent_set - child_set).pop()
        ans.val = root

        # bfs 구현을 위한 deque 사용
        qu = deque()

        # root: 부모 노드 값
        # ans: 자식을 연결해야 할 TreeNode
        qu.append((root, ans))

        # bfs 시작
        while qu:
            parent, node = qu.popleft()

            # KeyError를 방지하고자 get 메서드 사용
            # 해당 값이 없다면 초기에 설정한 [0, 0]로 설정
            left = dit.get(parent, [0, 0])[0]
            right = dit.get(parent, [0, 0])[1]

            # 자식 노드가 있을 경우 TreeNode 해당 위치에 삽입
            # 해당 자식 노드가 부모 노드가 될 수 있으므로 qu에 삽입
            if left:
                node.left = TreeNode(left)
                qu.append((left, node.left))
            
            if right:
                node.right = TreeNode(right)
                qu.append((right, node.right))

        return ans