# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r, q, p = None, None, head

        while p:
            r = q
            q = p
            p = p.next

            q.next = r

        return q 