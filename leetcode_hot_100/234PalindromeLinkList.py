# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.frontPointer = head
        def reverse(current_node = head):
            if current_node is not None:
                if not reverse(current_node.next):
                    return False
                if self.frontPointer.val != current_node.val:
                    return False
                self.frontPointer = self.frontPointer.next

            return True
        return reverse()
            