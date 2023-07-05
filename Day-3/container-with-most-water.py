class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n-1
        n = len(height)
        while left <=right:
            ans = max(ans,(right-left) * min(height[left],height[right]) )
            if height[left] < height[right]:
                left+=1
            else:
                
                right-=1
        return ans