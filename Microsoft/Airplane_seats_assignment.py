class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n==1:return float(1)
        #  for the nth guy just two option are available that is his own or someone elses:
        # we have two case scenarios first is the guy he randomly sits on someones seat and when the person arrive either that person ask the first guy to move his to seat if he seated on his or the second guy have his seat vacant 
        return float(0.5)