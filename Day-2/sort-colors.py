class Solution:
    def sortColors(self, a: List[int]) -> None:
        left = 0
        right = 0
        n = len(a) - 1
        while right <= n:
            if a[right] == 0:
                a[left], a[right] = a[right], a[left]
                left += 1
                right += 1
            elif a[right] == 1:
                right += 1
            else:
                a[n], a[right] = a[right], a[n]
                n -= 1
        return a
