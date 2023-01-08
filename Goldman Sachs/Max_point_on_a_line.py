class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # check if the line equation formed from combinations of any two points in the given array satisfies with the number points in the given points array. i.e return the maximum points that satisfies the line equation
        p = len(points) 
        if p == 1: return 1
        elif p == 2: return 2
        else:
            ans = 0
            for i in list(combinations(points,2)):
                count = 0
                for j in points:
                    if (j[1] - i[0][1]) * (i[1][0] - i[0][0]) == (j[0] - i[0][0]) * (i[1][1] - i[0][1]):
                        count += 1
                ans = max(ans, count)
            return ans