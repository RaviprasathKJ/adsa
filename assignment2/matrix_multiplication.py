def matrix_chain_multiplication(matrix_dimensions):
    n = len(matrix_dimensions) - 1  # Number of matrices
    m = [[0] * n for _ in range(n)]  # Initialize the memoization table for minimum multiplications
    s = [[0] * n for _ in range(n)]  # Initialize the table for split positions

    # Initialize the memoization table and split table
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = 0  # Set to 0 because matrices are already in the correct order
            s[i][j] = i  # Store the split position

    return m, s

def optimal_parenthesization(s, i, j, matrix_names):
    if i == j:
        return matrix_names[i]
    else:
        left = optimal_parenthesization(s, i, s[i][j], matrix_names)
        right = optimal_parenthesization(s, s[i][j] + 1, j, matrix_names)
        return f"({left} x {right})"

# Given list of matrices with dimensions
matrix_dimensions = [(2, 3), (3, 4), (4, 2)]
matrix_names = ['A', 'B', 'C']
m, s = matrix_chain_multiplication(matrix_dimensions)

# Find the optimal parenthesization
optimal_sequence = optimal_parenthesization(s, 0, len(matrix_dimensions) - 2, matrix_names)
minimum_scalar_multiplications = m[0][len(matrix_dimensions) - 3]

print("Optimal Parenthesization:", optimal_sequence)
print("Minimum number of scalar multiplications:", minimum_scalar_multiplications)
