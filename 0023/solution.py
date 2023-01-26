from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        initial = ListNode(0)
        curr = initial
        q = PriorityQueue()

        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))

        while not q.empty():
            _, i, min_node = q.get()
            if min_node.next:
                q.put((min_node.next.val, i, min_node.next))
            curr.next = min_node
            curr = curr.next

        return initial.next