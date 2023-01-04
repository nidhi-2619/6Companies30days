from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # reverse pair
        a = SortedList()
        ans = 0
        for i,j in zip(nums1, nums2):
            ans += a.bisect_right(i - j + diff)
            a.add(i - j)
        return ans