# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sumi = -float('inf')
        def dfs(rot):
            if not rot:
                return 0
            l = max(0,dfs(rot.left))
            r = max(0,dfs(rot.right))
            sumo = rot.val + l + r
            nonlocal sumi
            sumi = max(sumo,sumi)
            return max(l+rot.val,r+rot.val)
        a = dfs(root)
        return sumi
