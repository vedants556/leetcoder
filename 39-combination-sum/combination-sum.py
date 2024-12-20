class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i , curr , tot):
            if tot == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or tot > target:
                return
            
            curr.append(candidates[i])
            dfs(i , curr, tot + candidates[i])
            curr.pop()
            dfs(i + 1 , curr , tot)
        dfs(0 , [] , 0)
        return res