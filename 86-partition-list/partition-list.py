# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)

        before_tail = before
        after_tail = after

        while head:
            if head.val < x:
                before_tail.next = head
                before_tail = before_tail.next
            else:
                after_tail.next = head
                after_tail = after_tail.next

            head = head.next

        after_tail.next = None
        before_tail.next = after.next

        return before.next