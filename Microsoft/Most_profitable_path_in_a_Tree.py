class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs(node, start, visited):              
            maxi = float('-inf')
            node_to_bob = 0
            visited[node] = True
            for i in tree[node]:
                if not visited[i]:
                    cur, to_bob = dfs(i,start + 1, visited)
                    if not node_to_bob:
                        node_to_bob = to_bob
                    maxi = max(maxi, cur)
                                    
            if maxi == float('-inf'):
                if node == bob:
                    return 0, 1
                else:
                    return amount[node], 0
                
                
            if node == bob:
                return (maxi, 1)
            elif node_to_bob > 0:
                if start > node_to_bob:
                    return maxi, node_to_bob + 1
                elif start == node_to_bob:
                    return maxi + amount[node] // 2, node_to_bob + 1
                else:
                    return maxi + amount[node], node_to_bob + 1
            else:
                return maxi + amount[node], 0
            
        
        n = len(amount)
        tree = defaultdict(list)
        for parent, child in edges:
            tree[parent].append(child)
            tree[child].append(parent)            
        
        visited = [False for i in range(n)]
        profit, to_bob = dfs(0, 0, visited)
        return profit