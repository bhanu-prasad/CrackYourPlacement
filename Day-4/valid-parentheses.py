class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if len(s)<=1:
            return False
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]" and len(stack)>0:
                if (i==")" and stack[-1]=='(') or (i=="}" and stack[-1]=='{') or (i=="]" and stack[-1]=='['):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack):
            return False
        return True

