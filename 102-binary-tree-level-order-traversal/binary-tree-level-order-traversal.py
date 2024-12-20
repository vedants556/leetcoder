# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        
        if root:
            q.append(root)

        while q:
            level = []
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            # Append the current level to the result if it's non-empty
            if level:
                res.append(level)
                
        return res