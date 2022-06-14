# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # will go through list one at a time
    slow = head
    # will go through list twice as fast
    fast = head
    
    # once fast meets the end, slow will be in the middle
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow