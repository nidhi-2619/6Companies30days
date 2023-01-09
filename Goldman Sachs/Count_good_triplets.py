class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        ds = [0] * n
        q = []
        
		# Build index map of nums2
        for i in range(n):
            ds[nums2[i]] = i
            
        for p1 in range(n):
            p2 = ds[nums1[p1]] # Position of nums1[p1] in nums2
            i = bisect.bisect(q, p2) # Position smaller than this one so far
            q.insert(i, p2)
            before = i
            after = n-1 - p1 - p2 + before # Based on number of unique values before and after are the same
            ans += before * after
            
        return ans