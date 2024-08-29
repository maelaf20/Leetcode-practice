# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = {}
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr in hashset:
                return curr
                break
            else:
                hashset[curr] = 1
            curr = curr.next
        return None
        