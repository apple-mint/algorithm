# 1110. Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/?envType=daily-question&envId=2024-07-17

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # 노드 최하단까지 탐색하면서 삭제해야 하는 노드인지 아닌지 확인하는 함수
    # 후위 순회로 왼쪽 자식 노드, 오른쪽 자식 노드, 부모 노드 순으로 탐색
    def search_delete(self, node: TreeNode, to_delete: List[int], forest: List[TreeNode]) -> TreeNode:
        
        # 만약 더이상 내려갈 값이 없으면 종료
        if not node:
            return None
        
        # 내려갈 값이 있을 경우 왼쪽 또는 오른쪽 노드를 탐색
        # 만약 None이 반환되었을 경우 더이상 내려갈 값이 없거나
        # 부모 노드가 삭제되어야 하는 노드라 연결이 끊긴 것
        # 그 값이 있을 경우, 즉 TreeNode형태로 왔을 경우
        # 노드 연결이 유지된 상태로 탐색을 진행해야 한다는 의미
        node.left = self.search_delete(node.left, to_delete, forest)
        node.right = self.search_delete(node.right, to_delete, forest)

        # 만약 부모 노드가 삭제되어야 하는 값인 경우
        # 그 자식 노드들이 존재한다면 반환된 TreeNode를 추가
        if node.val in to_delete:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)

            # 연결이 끊어졌으므로 TreeNode 형태가 아닌 None 반환
            return None
        
        # 만약 부모 노드가 삭제되는 것이 아니면
        # 그 노드 연결 자체가 유지된 상태로 전달되어야 하므로
        # 해당 TreeNode 형태를 반환
        return node


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        # 값을 담을 ans 준비
        ans = []

        # forest를 구하기 위해 search_delete 함수 실행
        # 만약 값이 있다면 forest에 추가되지 않은 TreeNode가 존재한다는 의미
        node = self.search_delete(root, to_delete, ans)

        # 노드가 도중에 끊어지지 않아 그대로 node가 반환되는 경우
        # ans에 추가되지 않았으므로 ans에 추가
        if node:
            ans.append(node)

        return ans