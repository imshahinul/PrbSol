# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        c = 0
        head = self.head
        out = 0
        while head:
            c += 1
            r = random.randint(1, c)
            if c == r:
                out = head.val
            head = head.next
        return out

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()