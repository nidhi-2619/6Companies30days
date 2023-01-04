from math import gcd 
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        # finding the element smaller than gcd 
        g = gcd(*numsDivide)
        mini = float('inf')
        for i in nums:
            if g%i==0:
                mini = min(i,mini)
        if mini==float('inf'):return-1
        count=0
        for i in nums:
            if i<mini:
                count+=1
        return count        