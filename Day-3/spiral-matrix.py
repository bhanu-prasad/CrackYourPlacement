class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        ans = []
        seen = [[False]*m for _ in range(n)]
        x=y = 0
        di = 0
        for i in range(m * n):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dr[di]
            cc = y + dc[di]
 
            if (0 <= cr and cr < n and 0 <= cc and cc < m and not(seen[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return ans