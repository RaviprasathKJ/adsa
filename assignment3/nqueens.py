def solve_n_queens(N):
    def is_safe(board, row, col):
        # Check the current column for queens
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the left upper diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check the right upper diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == N:
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    solutions = []
    board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

N = int(input())
solutions = solve_n_queens(N)
print_solutions(solutions)


# time complexity
# The number of recursive calls made by the backtrack function is bounded by the number of possible placements of queens, which is typically much less than N^2 because each row can only have one queen. Therefore, the time complexity can be approximated as O(N!), where N is the size of the chessboard.