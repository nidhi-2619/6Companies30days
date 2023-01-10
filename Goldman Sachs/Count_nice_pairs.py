class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
# Rearrange nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) to get nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
# For each n in nums, keep track of nums[i] - rev(nums[i])
# Create Counter for these diffs
# Say n numbers have the same diff, then the number of nice pairs is 1+2+...+n = n(n-1)//2
        return  sum(count*(count-1)//2 for count in Counter(n - int(str(n)[::-1]) for n in nums).values()) % (10**9 + 7)