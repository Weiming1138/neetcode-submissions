class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                current_val = board[r][c]
                
                if current_val == ".":
                    continue

                box_index = (r//3) * 3 + (c//3)

                if (current_val in rows[r]):
                    return False
                elif (current_val in cols[c]):
                    return False
                elif (current_val in box[box_index]):
                    return False

                rows[r].add(current_val)
                cols[c].add(current_val)
                box[box_index].add(current_val)
        
        return True





