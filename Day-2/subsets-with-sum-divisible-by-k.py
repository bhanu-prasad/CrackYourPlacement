class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sumi = 0
        counter = 0
        mp =  [1]+[0]*(k-1)
        for i in range(len(nums)):
            sumi+=nums[i]
            
            rem= (sumi)%k
            if mp[rem]:
                counter+=mp[rem]
            
            mp[rem] += 1
        return counter