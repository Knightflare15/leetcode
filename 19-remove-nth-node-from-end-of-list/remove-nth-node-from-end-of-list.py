# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur= head
        fast = head
        prev = ListNode()
        prev.next = cur
        while fast and n>0:
            fast=fast.next
            n-=1
        if n>0:
            return head
        if not fast:
            return head.next
        while fast:
            prev = cur
            cur = cur.next
            fast = fast.next
        prev.next = cur.next
        return head
        