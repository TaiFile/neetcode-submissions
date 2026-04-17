class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # --- 1) Verificar linhas ---
        for i in range(n):
            dataRow = []
            for j in range(n):
                value = board[i][j]
                if value != ".":
                    if value in dataRow:
                        return False
                    dataRow.append(value)

        # --- 2) Verificar colunas ---
        for j in range(n):
            dataColumn = []
            for i in range(n):
                value = board[i][j]
                if value != ".":
                    if value in dataColumn:
                        return False
                    dataColumn.append(value)

        # --- 3) Verificar blocos 3x3 ---
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if not self.isValidBox(i, j, board):
                    return False

        return True

    def isValidBox(self, start_row: int, start_col: int, board: List[List[str]]) -> bool:
        boxContent = []
        for i in range(3):
            for j in range(3):
                row = start_row + i
                col = start_col + j
                value = board[row][col]
                if value != ".":
                    if value in boxContent:
                        return False
                    boxContent.append(value)
        return True