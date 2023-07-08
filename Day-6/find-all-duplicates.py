class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        has = [0]*len(nums)
        ans = []
        for i in nums:
            if has[i-1] == 1:
                ans.append(i)
            else:
                has[i-1] =1
        return ans