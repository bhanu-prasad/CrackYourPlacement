
#https://leetcode.com/problems/subarray-sum-equals-k/description/
def subarraySum(self, nums: List[int], k: int) -> int:
    d={0:1}
    sum=0
    count=0
    for i in range(len(nums)):
        sum=sum+nums[i]
        if sum-k in d:
            count=count+d[sum-k]
        if sum in d:
            d[sum]=d[sum]+1
        else:
            d[sum]=1
    return count