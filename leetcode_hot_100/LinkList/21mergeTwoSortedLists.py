# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2 = list1,list2
        
        dummy = ListNode() # 哨兵节点，简化边界处理
        curr = dummy # 工作指针，指向链表尾部

        # 合并两个有序链表
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        
        curr.next = p1 if p1 else p2

        return dummy.next
        
        