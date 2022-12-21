# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr = ""
        while l1 != None:
            arr = arr + str(l1.val)
            l1 = l1.next
        arr = arr[-1::-1]
        arr2 = ""
        while l2 != None:
            arr2 = arr2 + str(l2.val)
            l2 = l2.next
        arr2 = arr2[-1::-1]
        thoma = int(arr) + int(arr2)
        thoma = str(thoma)
        thoma = thoma[-1::-1]
        dummy = ListNode(0)
        head = dummy
        for i in thoma:
            newNode = ListNode(i)
            head.next = newNode
            head = head.next
        return dummy.next