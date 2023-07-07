
#recursion

n=3
dp={}
def solve(n):
    if n==0:
        return 1
    if n<0:
        return 0
    if n in dp:
        return dp[n]
    l=solve(n-1)
    r=solve(n-2)
    dp[n]=l+r
    return l+r
c=solve(n)
print(c) 

#tabulation

n=3
d={}
d[0]=1
for i in range(1,n+1):
    l=d[i-1]
    r=0
    if i>1:
        r=d[i-2]
    d[i]=l+r 
print(d[n])

#space optimization

n=3
first=1
second=0
for i in range(1,n+1):
    l=first
    r=0
    if i>1:
        r=second
    curr=l+r
    second=first
    first=curr
print(first)
