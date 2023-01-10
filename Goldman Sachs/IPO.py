class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # merge captial and profit in a single list
        costs = [(capital[i],profits[i]) for i in range(len(profits))]
        # sort it based on captial
        costs.sort()
        idx = 0
        max_q = []
        # iterate till we choose k projects
        while k!=0: 
            # keep adding it to max q till we reach a cost > w
            while idx<len(costs) and costs[idx][0]<=w:
                heapq.heappush(max_q,-costs[idx][1]) 
                idx+=1
            # pop the max element and add it to current cost. 
            if len(max_q)>0:
                w+=(-heapq.heappop(max_q))
            k-=1
        return w