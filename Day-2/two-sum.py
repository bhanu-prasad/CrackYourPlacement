class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if str(diff) in mp:
                return [mp[str(diff)], i]
            mp[str(nums[i])] = i
        return []
