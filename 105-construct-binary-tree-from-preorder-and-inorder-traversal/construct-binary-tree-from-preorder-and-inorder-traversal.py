# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeR(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder:
                return None
            root = TreeNode()
            root.val = preorder[0]
            l = 0
            while l<len(inorder) and inorder[l]!=root.val:
                l+=1
            root.left = self.buildTreeR(preorder[1:l+1],inorder[0:l])
            root.right = self.buildTreeR(preorder[l+1:],inorder[l+1:])
            return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        return self.buildTreeR(preorder,inorder)
        

        