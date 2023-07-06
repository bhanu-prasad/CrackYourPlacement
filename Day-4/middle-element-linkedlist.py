# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp.next != None:
            temp = temp.next
            n+=1
        n = math.ceil(n/2)
        # print(n,head)
        for _ in range(1,n+1):
            head = head.next
        return head