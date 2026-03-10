# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        tmp = ListNode(1,None)
        head = tmp
        tmp.next = None
        while cur1 and cur2:
                print(head)
                if cur1.val <= cur2.val:
                    tmp.next = cur1
                    tmp=  tmp.next
                    cur1 = cur1.next
                    print(cur1)
                else:
                    tmp.next = cur2
                    tmp=tmp.next
                    cur2 = cur2.next
                    print(cur2)
        while cur1:
            tmp.next = cur1
            cur1=cur1.next
            tmp = tmp.next
        while cur2:
            tmp.next = cur2
            cur2 = cur2.next
            tmp = tmp.next
        return head.next
