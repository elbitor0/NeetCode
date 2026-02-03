from typing import List
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_check_list = [set() for _ in range(9)]
        lines_check_list = [set() for _ in range(9)]
        box_check_list = [set() for _ in range(9)]
        for i, line in enumerate(board):
            for j, case in enumerate(line):
                box_number =j//3 + 3*(i//3) 
                if case != '.' and (case in cols_check_list[j] or case in box_check_list[box_number] or case in lines_check_list[i]):
                    return False
                else:
                    cols_check_list[j].add(case)
                    lines_check_list[i].add(case)
                    box_check_list[box_number].add(case)
        return True