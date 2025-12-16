# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, dummy.next
        while curr and curr.next :
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr

            prev = curr
            if prev :
                curr = prev.next
            else :
                curr = None

        return dummy.next