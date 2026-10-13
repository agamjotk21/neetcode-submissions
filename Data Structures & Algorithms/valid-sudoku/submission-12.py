class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def getCurrBox(board, sRow, sCol, boxSize) -> List:
            valsInGrid = []
            for row in range(sRow, sRow + boxSize): 
                for col in range(sCol, sCol + boxSize): 
                    valsInGrid.append(board[row][col])
            return valsInGrid



        currCheck = set() #curr row, column, mini Grid

        for row in board: 
            for num in row: 
                if num.isdigit():
                    if num not in currCheck: 
                        currCheck.add(num)
                    else: 
                        return False 
            currCheck = set()
        currCheck = set()
        #columns: 
        rows, cols = len(board), len(board[0])
        for col in range(cols):
            for row in range(rows):
                num = board[row][col]
                if num.isdigit():
                    if num not in currCheck: 
                        currCheck.add(num)
                    else: 
                        return False 
            currCheck = set()
        currCheck = set()
        
        #grid
        for row in range(0, rows, 3): 
            for col in range(0, cols, 3):
                currBox = getCurrBox(board, row, col, 3)
                for num in currBox:
                    if num.isdigit():
                        if num not in currCheck: 
                            currCheck.add(num)
                        else: 
                            return False
                currCheck = set()
        return True 
                    

        
        


                

        