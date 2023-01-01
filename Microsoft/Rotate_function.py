class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # intuition 
        # current function = previous function +sum of nums -(n*nums[i])
        n = len(nums)
        summ = sum(nums)
        prev = 0
        for i,j in enumerate(nums):
            prev+=i*j
        maxi = prev    
        for i in range(n-1,0,-1):
            curr = prev+summ-(n*nums[i])
            maxi = max(curr,maxi)
            prev = curr
        return maxi    