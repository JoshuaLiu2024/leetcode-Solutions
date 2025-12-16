# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_1:
    # 暴力法，首先根据输入的l1 l2两个链表计算出两个整数，加和，然后构建出新的链表。
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getnum(l):
            num = 0
            base = 1
            while l:
                num += l.val * base
                base *= 10
                l = l.next
            return num

        sum_num = getnum(l1) + getnum(l2)
        
        if sum_num == 0 :
            return ListNode(0)

        answer = ListNode()
        working_point = answer
        while sum_num != 0:
            # 建立新节点
            new_node = ListNode()
            working_point.next = new_node
            working_point = new_node

            # 给新节点的val区填入当前位置的数值
            temp = sum_num % 10
            working_point.val = temp
            sum_num = sum_num // 10
        
        return answer.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 模拟逐位加法
        curr = dummy = ListNode() # dummy哨兵节点，建立新链表存储答案
        carry = 0 # 进位标志，说明上一次扫描是否发生了进位

        while l1 or l2 or carry :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next
        
        return dummy.next