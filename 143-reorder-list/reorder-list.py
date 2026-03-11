# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        cur = head
        n=1
        while cur:
            cur = cur.next
            if cur:
                stack.append(cur)
                n+=1
        n = n//2
        cur = head
        tmp = head
        while cur and n>0:
            tmp = cur.next
            cur.next = stack.pop(-1)
            cur=cur.next
            cur.next = tmp
            cur = tmp
            n-=1
        if cur:
            cur.next = None
        return head
        
        
        