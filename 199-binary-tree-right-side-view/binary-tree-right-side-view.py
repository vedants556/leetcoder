# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if root is None:
            return res  # If the tree is empty, return an empty list
        
        # Initialize queue with root node if it's not None
        q = deque([root])

        while q:
            rightSide = None
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node  # Update rightmost node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            # After processing the level, append the rightmost node to the result
            if rightSide:
                res.append(rightSide.val)
        
        return res