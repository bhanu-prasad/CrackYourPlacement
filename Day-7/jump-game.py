class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= final - i:
                final = i
        
        return True if final == 0 else False
            
            

        
