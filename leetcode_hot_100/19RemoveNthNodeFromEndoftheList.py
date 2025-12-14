# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        list_length = 0
        while p != None :
            list_length += 1
            p = p.next
        
        if n == list_length :
            return head.next
        
        prev = head
        for i in range(list_length - n - 1):
            prev = prev.next
        
        prev.next = prev.next.next

        return head
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast :
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next