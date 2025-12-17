# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 暴力法：先把所有元素重新保存在一个列表中，使用.sort()函数排序，然后重建链表
        if not lists :
            return None
        
        temp_list = list()
        for head in lists :
            
            while head :
                temp_list.append(head.val)
                head = head.next
        temp_list.sort()

        dummy = ListNode()
        p = dummy
        for val in temp_list :
            new_node = ListNode(val)
            p.next = new_node
            p = new_node

        return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 经典法：按顺序两两合并
        if not lists :
            return None
        
        def merge(list1, list2):
            p, q = list1, list2
            dummy = ListNode()
            curr = dummy
            while p and q :
                if p.val <= q.val :
                    new_node = ListNode(p.val)
                    p = p.next
                else :
                    new_node = ListNode(q.val)
                    q = q.next

                curr.next = new_node
                curr = new_node
            
            if not p :
                curr.next = q
            else :
                curr.next = p

            return dummy.next

        ans = len(lists)
        list_dummy = lists[0]
        for i in range(ans-1) :
            list1 = lists[i+1]
            list_dummy = merge(list_dummy, list1)

        return list_dummy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 分治合并法
        if not lists :
            return None
        
        def merge(list1, list2):
            p, q = list1, list2
            dummy = ListNode()
            curr = dummy
            while p and q :
                if p.val <= q.val:
                    curr.next = p
                    p = p.next
                else :
                    curr.next = q
                    q = q.next
                curr = curr.next
            
            if not p :
                curr.next = q
            else :
                curr.next = p

            return dummy.next

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        return lists[0]
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_4:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 优先队列法:最小堆
        dummy = ListNode()
        curr = dummy

        import heapq
        heap = []

        # 初始化堆：把每个非空链表的第一个节点压入堆
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 如果该节点还有下一个节点，加入堆
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next