class Solution:
    # Maintain 2 hashmaps
    # First one stores the frequency of each num in nums
    # Second one stores 3 or more length subarrays of nums ending with a particular num
    # Cases when we iterate to a n in nums - 
    # 1. there alredy exists a subarray ending with n - 1 -> add n to it
    # 2. there is no n - 1 ending subarray present - > create one subarray of n, n + 1, n + 2
    # 3. n + 1 and n + 2 are not present - > answer not possible return False
    # If all above cases pass without returning false you have a valid nums which can be divided hence return True
    
    def isPossible(self, nums: List[int]) -> bool:
        hm1 = Counter(nums)
        hm2 = defaultdict(int)
        
        for num in nums:
            if hm1[num] == 0: continue
            
            if num - 1 in hm2 and hm2[num - 1] > 0:
                hm2[num - 1] -= 1
                hm2[num] += 1
            
            elif num + 1 in hm1 and num + 2 in hm1 and hm1[num + 1] > 0 and hm1[num + 2] > 0:
                hm2[num + 2] += 1
                hm1[num + 1] -= 1
                hm1[num + 2] -= 1
            
            else:
                return False
            
            hm1[num] -= 1
        
        return True