# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        dummy_head, count = head, 0
        while dummy_head:
            dummy_head = dummy_head.next
            count += 1

        mid = count // 2

        # split the linked list from the middle
        dummy, count = head, 0
        while mid > 0:
            dummy = dummy.next
            mid -= 1
        
        second_half = dummy.next
        dummy.next = None

        
        # reverse the second half      
        prev, curr = None, second_half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the array
        res = ListNode(0)
        dummy_res = res

        while prev and head:
            dummy_res.next = head
            dummy_res = dummy_res.next
            head = head.next

            dummy_res.next = prev
            dummy_res = dummy_res.next
            prev = prev.next

        if head:
            dummy_res.next = head
        if prev:
            dummy_res.next = prev

        head = res.next

        
