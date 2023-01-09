m= 10**9+7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        dp[0]=1
        count = 0
        for i in range(1,n):
            dp[i]=count+dp[i-delay]-dp[i-forget]
            count=dp[i]
        return sum(dp[n-forget:])%m 