class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par, visit):
            if node in visit:
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node, visit):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set() 
            
            if dfs(u, -1, visit):
                return [u, v]
        return []
