class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # the large rectangle area should be equal to the sum of small rectangles
# count of all the points should be even, and that of all the four corner points should be one
        s = set()
        area = 0
        #findind the coordinates of each rectangle
        for r in rectangles:
            tl = (r[0], r[3]) #top-left 
            tr = (r[2], r[3]) #top-right
            bl = (r[0], r[1]) #bottom-left
            br = (r[2], r[1]) #bottom-right
            #area calculation of rectangle
            area += (r[2] - r[0]) * (r[3] - r[1])
            #overlapping points should be removed
            for i in [tl, tr, bl, br]:
                if i not in s:
                    s.add(i)
                else:
                    s.remove(i)
        # not able to form a rectangle            
        if len(s) != 4:
            return False
        s = sorted(s)
        start = s.pop(0)
        end = s.pop()
        return area == (end[0] - start[0]) * (end[1] - start[1])