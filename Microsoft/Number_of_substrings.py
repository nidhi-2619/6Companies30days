class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        # we will track the recent indices of a,b,c
        ri_a,ri_b,ri_c = -1,-1,-1 
        for i,val in enumerate(s):
            if val=='a':
                ri_a = i
            elif val=='b':
                ri_b = i
            else:
                ri_c = i
            # so that the minimum window size is maintained i.e 3 
            if i>=2:
                # one is added to get the actual index
                count+=min(ri_a,ri_b,ri_c)+1 
        return count      