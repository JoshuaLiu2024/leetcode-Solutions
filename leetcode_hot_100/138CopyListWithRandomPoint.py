"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 哈希表
        if not head :
            return None
        
        old_to_new = dict()
        curr = head
        # 创建所有节点，并存储在哈希表中
        while curr :
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        # 设置这些新节点的next和random指针，即使链表成型
        while curr :
            new_node = old_to_new[curr]
            new_node.next = old_to_new.get(curr.next)
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]