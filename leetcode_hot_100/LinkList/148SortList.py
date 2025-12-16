# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = list()
        curr = head
        while curr :
            temp.append(curr.val)
            curr = curr.next
        
        temp.sort()

        dummy = ListNode()
        curr = dummy
        for val in temp :
            new_node = ListNode(val)
            curr.next = new_node
            curr = new_node

        return dummy.next