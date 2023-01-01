class Solution:
    def twist(self,i,k,n,ans,ds):
        # base case
        if k==0 and n==0:
             ans.append(ds.copy())
             return
        # if n or k becomes negative we have to return
        if k<0 or n<0:
            return
        # if i gets more than 9 the given condition fails we return
        if i>9:
            return   
        # picking the number
        ds.append(i)
        self.twist(i+1,k-1,n-i,ans,ds)
        # backtracking
        ds.pop()
        #not picking element
        self.twist(i+1,k,n,ans,ds)



    def combinationSum3(self, k: int, n: int) :
        ans = []
        ds = []
        self.twist(1,k,n,ans,ds)
        return ans