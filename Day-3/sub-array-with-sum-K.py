from collections import defaultdict

class Solution:
    def subarraySum(self, a: List[int], K: int) -> int:
        n = len(a)
        hash = defaultdict(lambda: 0)
        count = 0
        sum = 0
        for i in range(n):
            sum += a[i]
            if sum == K:
                count += 1
            if (sum - K) in hash:
                count += hash[sum - K]
            hash[sum] += 1
        return count