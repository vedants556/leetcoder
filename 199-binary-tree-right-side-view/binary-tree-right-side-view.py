class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # This will store the right side view

        # Return empty list if the tree is empty
        if root is None:
            return res

        # Initialize a deque to perform BFS
        q = deque([root])

        # Perform BFS to explore the tree level by level
        while q:
            rightSide = None  # Placeholder to store the rightmost node at the current level
            # Process all nodes at the current level
            for i in range(len(q)):
                node = q.popleft()  # Pop the leftmost node from the queue

                if node:
                    rightSide = node  # Update rightSide to the latest node encountered

                    # Add the left and right children to the queue for the next level
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            # After processing all nodes at the current level, add the rightmost node to the result
            if rightSide:
                res.append(rightSide.val)

        return res  # Return the right side view of the tree