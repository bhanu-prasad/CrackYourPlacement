class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = ""
        while head:
            ans+=str(head.val)
            head = head.next
        return int(ans,2)