class Solution:
    def longestPrefix(self, s: str) -> str:
        # KMP Algorithm
        n = len(s)
        LPS = [0]*n
        i = 0
        for j in range(1,n):
            while s[j]!= s[i] and i>0:
                i = LPS[i-1]
            if s[j]==s[i]:
                LPS[j]=i+1
                i+=1
        return s[:LPS[-1]]     