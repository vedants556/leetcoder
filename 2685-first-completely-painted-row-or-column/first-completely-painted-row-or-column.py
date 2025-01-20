from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        # Create a map from matrix value to its position
        mat_to_position = {}
        for r in range(ROWS):
            for c in range(COLS):
                mat_to_position[mat[r][c]] = (r, c)

        # Track the number of occurrences of each number in rows and columns
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        # Iterate through the array and check for completion
        for i in range(len(arr)):
            r, c = mat_to_position[arr[i]]
            row_cnt[r] += 1
            col_cnt[c] += 1

            # Check if either the row or column is complete
            if row_cnt[r] == COLS or col_cnt[c] == ROWS:
                return i

        return -1  # If no complete row or column is found
