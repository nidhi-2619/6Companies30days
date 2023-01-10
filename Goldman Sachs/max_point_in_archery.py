class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:  
        result = [0]*12
        ans = 0
        S = [0]
        for i in range(12):
            S.append(S[-1] + i)

        def dfs(idx, path, left, score):
            nonlocal ans, result
            
            if score+S[idx+1] < ans:
                return

            if idx == -1 or left == 0:
                if score > ans:
                    result = path[:]
                    # add remaining arrows
                    result[0] += left
                    ans = score
                return
            
            # bob wins
            if left > aliceArrows[idx]:
                path[idx] = aliceArrows[idx]+1
                dfs(idx-1, path, left-aliceArrows[idx]-1, score+idx)
                path[idx] = 0
            
            # alice wins
            dfs(idx-1, path, left, score)

        path = [0]*12
        dfs(11, path, numArrows, 0)
        
        return result
        