class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        left = 0
        right = M-1
        ans = float("inf")
        while right < N:
            ans = min(ans,A[right]-A[left])
            right+=1
            left+=1
        return ans
            