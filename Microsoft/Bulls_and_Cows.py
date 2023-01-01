class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls= 0
        cows = 0
        s,g = {},{}
        for i in secret:
            s[i]=s.get(i,0)+1
        for i in guess:
            g[i]=g.get(i,0)+1
        for i in g:
            if i in s:
                cows+=min(g[i],s[i])
        for i,j in zip(secret,guess):
            if j in secret :
                if i==j:
                    bulls+=1  
        return f'{bulls}A{cows-bulls}B'        