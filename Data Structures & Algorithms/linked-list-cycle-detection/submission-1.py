# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        elementos = []
        while curr:
            if curr in elementos:
                return True
            elementos.append(curr)
            curr = curr.next

        return False