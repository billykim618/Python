class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode([2, 4, 3])
l2 = ListNode([5, 6, 4])

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # val = 0
        # while l1.next != None:
        #     if l1.val + l2.val > 9:
        #         l3 = ListNode((l1.val + l2.val) % 10)
        #     else: l3 = ListNode(l1.val + l2.val)
        #     l1 = l1.next
        #     l2 = l2.next
        #     l3 = l3.next
        print(l1)
#         l3 = ListNode(l1.val + l2.val)

#         # return l3
#         return l1.next

    addTwoNumbers(l1, l1, l2)
