# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    height = 0
    head = None
    def hasNode(self,root,node):
        if not root:
            return False
        if root == node:
            return True
        K = False
        if root.left:
            K = K or self.hasNode(root.left,node)
        if root.right:
            K = K or self.hasNode(root.right,node)
        return K
    def traversal(self,p,q,root,h):
        if not root:
            return
        key = self.hasNode(root,p) and self.hasNode(root,q)
        self.traversal(p,q,root.right,h+1)
        self.traversal(p,q,root.left,h+1)
        if key  == True:
            if h>self.height:
                self.head = root
                self.height = h
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            self.height = -1
            self.head = None
            self.traversal(p,q,root,0)
            return self.head