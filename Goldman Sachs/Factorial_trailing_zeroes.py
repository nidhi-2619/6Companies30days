class Solution:  
    def trailingZeroes(self, n: int) -> int:
        # count the no of 5 in the factorize solution as 5*2 give 10 
        # there will be lot of 2 as compare to 5 and the number present less will be the deciding factor
        # return n//5+n//25+n//125+n//625+n//3125(another solution)
        # 5^k <=n
        #  5^k = n
        # k = log n base 5
        count = 0
        i=5
        while i<=n:
            count+=n//i
            i*=5
        return count
        
        


            