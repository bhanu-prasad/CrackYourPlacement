class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(s,n,l,openc,closec):
            print(s)
            if openc>n or closec>openc:
                return
            if openc<n:
                solve(s+"(",n,l,openc+1,closec)
            if openc>=closec:
                solve(s+")",n,l,openc,closec+1)
            if openc==closec==n:
                print(s)
                l.append(s[:])
        l=[]
        openc=1
        closec=0
        solve("(",n,l,openc,closec)
        return l
