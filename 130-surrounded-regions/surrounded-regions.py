class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if board[r][c] != 'O':
                return

            board[r][c] = 'T'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Left and Right borders
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)

            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Top and Bottom borders
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)

            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Flip and Restore
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == 'T':
                    board[r][c] = 'O'