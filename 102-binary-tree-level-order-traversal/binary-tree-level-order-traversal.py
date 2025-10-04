# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        h = 1
        res = []
        while q:
            if h==0:
                h = len(q)
                result.append(res)
                res = []
            node = q.popleft()
            if node and h>0:
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            h-=1
        if res:
            result.append(res)
        return result

        