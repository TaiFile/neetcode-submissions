# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        left = 0
        right = len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            nodes[right].next = nodes[left + 1]
            left += 1
            right -= 1
        nodes[left].next = None  # ✅ fecha a lista