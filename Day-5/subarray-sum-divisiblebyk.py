
#https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
d={0:1}
sum=0
c=0
nums =[-4,5]
k =10
for i in range(len(nums)):
    sum=sum+nums[i]
    rem=sum%k
    if rem in d:
        c=c+d[rem]
        d[rem]+=1
    else:
         d[rem]=1
print(d)
print(c)