# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev 指向前一个 group 的尾

        while True:
            # 检查从 prev.next 开始是否有 k 个节点
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next  # 不足 k 个，直接返回
            
            # 记录下一组的开始
            next_group = tail.next

            # 反转 [prev.next, tail]
            start = prev.next
            pre = None
            curr = start
            while curr != next_group:
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt

            # 连接：prev -> 新头（即 tail），原 start -> next_group
            prev.next = tail
            start.next = next_group

            # 移动 prev 到本组结尾（即原来的 start）
            prev = start

        return dummy.next