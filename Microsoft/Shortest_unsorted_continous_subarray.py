class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # # O(nlogn) approach
        # aux = sorted(nums)
        # start ,end=len(nums),0
        # for i,j in enumerate(nums):
        #     if nums[i]!=aux[i]:
        #         start = min(start,i)
        #         end = max(end,i)
        # if start==len(nums):
        #     return 0      
        # return end-start+1   
        n = len(nums)
        maxi,mini = nums[0],nums[-1]
        start,end =0,0
        # checking from end
        for i in range(n-2,-1,-1):
            if nums[i]>mini:
                start=i
            else:
                mini = nums[i]
        # checking from start
        for i in range(1,n):
            if nums[i]<maxi:
                end=i
            else:
                maxi = nums[i]     
        if start!=end:
            return end-start+1
        return 0                          