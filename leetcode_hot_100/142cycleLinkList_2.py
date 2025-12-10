# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break # 找到了相遇点，证明存在环，准备寻找环的进入点
        else:
            # 没有找到相遇点，说明没有环
            return None
        # 寻找相遇点
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        return ptr