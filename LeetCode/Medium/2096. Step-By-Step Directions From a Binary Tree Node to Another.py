# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/?envType=daily-question&envId=2024-07-16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # 최상단 노드에서 각각 시작점, 도착점까지의 경로를 구하기 위한 함수
    # 시작점 또는 도착점에 도착한 뒤 역순으로 타고 올라옴
    def getPath(self, node: Optional[TreeNode], value: int, path: List[str]) -> bool:
        
        # 시작점 또는 도착점에 도착할 경우 멈춤
        # 아래의 재귀함수에서 여태까지 다녀온 경로를
        # 미리 설정한 리스트에 넣을 수 있도록 True 값 반환
        if node.val == value:
            return True
        
        # if-elif로 조건을 설정한 이유는
        # 왼쪽 최하단까지 시작점 또는 도착점이 있는지 탐색 후
        # 그 다음 오른쪽 최하단으로 넘어가기 위함

        # 만약 왼쪽에 자식노드가 있고 시작점 또는 도착점이
        # 그 자식노드를 지나갔다면 L를 리스트에 삽입
        if node.left and self.getPath(node.left, value, path):
            path.append('L')

        # 만약 오른쪽에 자식노드가 있고 시작점 또는 도착점이
        # 그 자식노드를 지나갔다면 R를 리스트에 삽입
        elif node.right and self.getPath(node.right, value, path):
            path.append('R')

        # 재귀함수 내 path의 값이 갱신될 수 있도록 반환
        return path


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # start: 최상단 노드에서 시작점으로 가는 경로
        # dest: 최상단 노드에서 도착점으로 가는 경로
        # 미리 리스트를 설정한 이유는 최상단 노드가 시작점 또는 도착점일 경우
        # True 값을 반환해 bool은 길이가 없다는 TypeError가 뜨기 때문
        start = []
        dest = []

        # 최상단 노드에서 시작점, 또는 도착점으로 가는 경로 탐색
        # 반환되는 값 없이 각각 만든 리스트에 값이 저장됨
        self.getPath(root, startValue, start)
        self.getPath(root, destValue, dest)

        # 만약 start와 dest에 값이 있을 경우
        # 마지막에 있는 경로가 동일할 경우
        # 같은 경로를 지난 것이므로 해당 경로 제외
        while len(start) and len(dest):
            last_start = start.pop()
            last_dest = dest.pop()
            
            if last_start != last_dest:
                start.append(last_start)
                dest.append(last_dest)
                break             
        
        # start의 경로의 수가 자연수일 경우 도착점에 도달하기 위해
        # 부모 노드를 타고 올라가야 하므로 그 수만큼 'U' 추가
        # dest는 start에서 부모 노드까지 온 지점에서부터
        # 내려와야 하므로 역순으로 탐색된 dest를 역순정렬 후 추가
        # dest.reverse() 자체는 NoneType이므로
        # join이 지원하는 반복 가능한 객체로 만들기 위해 reversed 사용
        ans = ''.join('U' * len(start)) + ''.join(reversed(dest))

        return ans