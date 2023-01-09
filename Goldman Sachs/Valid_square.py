class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = set()
        a = []
        
        def getDist(p1, p2):
            x, y = p1[0] - p2[0], p1[1] - p2[1]
            d = x ** 2 + y ** 2
            dist.add(d)
            a.append(d)
        
		# find the 6 distances on the image
        getDist(p1, p2)
        getDist(p1, p3)
        getDist(p1, p4)
        getDist(p2, p3)
        getDist(p2, p4)
        getDist(p3, p4)
		# if the number of distances we found is not 2, can't be square
        if len(dist) != 2:
            return False
			
		# sort non-decreasingly to have 4 edge distances, and 2 diagonal distances
        a.sort()
        
		#  check condition 
        if a[0] == a[1] == a[2] == a[3]:
            if a[4] == a[5]:
                return True
        return False