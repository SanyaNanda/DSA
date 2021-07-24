n=int(input())
dp=[-1 for _ in range(n+1)]

def fib(n,dp):
    if n==0 or n==1:
        dp[n]=n
        return n
    if dp[n]!=-1:
        return dp[n]
    ans=fib(n-1,dp)+fib(n-2,dp)
    dp[n]=ans
    return ans 

fib(n,dp)
print(*dp)