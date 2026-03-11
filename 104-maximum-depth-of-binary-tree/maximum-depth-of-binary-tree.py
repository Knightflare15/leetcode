# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    height = 0
    def depth(self,root,h):
        if not root:
            return
        h+=1
        self.height = max(h,self.height)
        self.depth(root.left,h)
        self.depth(root.right,h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth(root,0)
        return self.height
