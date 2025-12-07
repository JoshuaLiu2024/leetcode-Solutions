# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 第一遍自己做想到的方法：首先计算两链表的长度，根据长度差先遍历较长的链表，
# 然后再同时移动两个工作指针，直到两工作指针指向同一个节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB :
            return None
        def getlength(head:ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        length_A = getlength(headA)
        length_B = getlength(headB)

        diff = length_A - length_B

        longer = None
        shorter = None
        if diff > 0:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA
            diff = 0 - diff
        
        r = longer
        t = shorter

        for i in range(diff):
            r = r.next
        
        while r != t:
            r = r.next
            t = t.next
        
        return r
            
# AI提出了新的算法：双指针法
# 原理：
# 如果两链表独有长度分别为a,b，共有长度为c，那么我们可以得到：
# 若两链表有交点，pA遍历A后再遍历B，pB遍历B后再遍历A，长度各自为a+c+b,b+c+a，两者相等。所以，当pA==pB时说明有交点且为两指针所指节点
# 若两链表无交点，两指针移动距离分别为：a+b,b+a，两者相等且此时二者同时指向None。
class Solution_2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA