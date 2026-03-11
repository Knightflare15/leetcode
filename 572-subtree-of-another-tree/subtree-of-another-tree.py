# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self,r1,r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        if r1.val != r2.val:
            return False
        return self.isEqual(r1.right,r2.right) and self.isEqual(r1.left,r2.left)
    def traversal(self,root,r2):
        
        answer = self.isEqual(root,r2)
        if root.left:
            answer = answer or self.traversal(root.left,r2)
        if root.right:
            answer = answer or self.traversal(root.right,r2)
        return answer

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        return self.traversal(root,subRoot)