class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minword = strs[0]
        for i in strs:
            if len(minword) > len(i):
                minword = i
        print(minword)
        commonind = -1
        for i in range(len(minword)):
            flag = 0
            for j in strs:
                if j[i] != minword[i]:
                    flag = 1
                    break
            if flag:
                break
            else:
                commonind+=1
        return "" if commonind == -1 else minword[:commonind+1]