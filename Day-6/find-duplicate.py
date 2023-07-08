class Solution:
    def findDuplicate(self, nums):
        has = [0]*len(nums)
        for i in nums:
            if has[i-1] == 1:
                return i
            else:
                has[i-1] =1
