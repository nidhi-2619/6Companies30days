class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       topo = [[] for _ in range(numCourses)]
       visit = [0 for _ in range(numCourses)]
       for i,j in prerequisites:
           topo[i].append(j)
       def dfs(x):
           if visit[x] ==-1:
               return False
           if visit[x] ==1:
               return True
           visit[x] = -1
           for i in topo[x]:
               if not dfs(i):
                   return False
           visit[x] = 1
           return True
       for i in range(numCourses):
           if not dfs(i):
               return False
       return True              