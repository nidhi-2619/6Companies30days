import collections 
import heapq
m = 10**9+7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for u,v,t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))
        times = [float('inf')]*n
        paths = [0]*n
        times[0] = 0
        paths[0] = 1
        dk = [(0,0)]
        while dk:
            curr_time,curr_node = heapq.heappop(dk)
            for v,t in graph[curr_node]:
                updated_time = curr_time + t
                if updated_time < times[v] :  
                    times[v] = updated_time
                    paths[v] = paths[curr_node]
                    heapq.heappush(dk,(updated_time,v))
                elif updated_time ==times[v]:
                    paths[v] += paths[curr_node]
        return paths[n-1]%m    