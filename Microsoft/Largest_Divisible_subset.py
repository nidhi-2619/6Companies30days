class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n= len(nums)
        if n==0:return []
        nums.sort()
        answer = [[i] for i in nums]
        for i in range(len(nums)):
            for j in range(i):
                if not nums[i]%nums[j] and len(answer[i])<len(answer[j])+1:
                    answer[i]=answer[j]+[nums[i]]
        return max(answer,key=len)      