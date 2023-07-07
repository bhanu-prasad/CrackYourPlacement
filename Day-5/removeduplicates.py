
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

i=0
j=1
nums = []
c=0
while i<len(nums) and j<len(nums):
    while j<len(nums) and nums[i]==nums[j] :
        j=j+1
    i=i+1
    if j>=len(nums):
        break
    nums[i],nums[j]=nums[j],nums[i]
    c=c+1
    j=j+1
print(nums,c+1)