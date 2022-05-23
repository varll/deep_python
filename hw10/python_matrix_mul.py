def python_matrix_mul(a_matrix, b_matrix):
    rows_a = len(a_matrix)
    cols_a = len(a_matrix[0])
    cols_b = len(b_matrix[0])

    c_matrix = [[0 for col in range(cols_b)] for row in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]

    return c_matrix


def python_chain_matrix_mul(matrices):
    result = matrices[0]
    for i in range(len(matrices)-1):
        result = python_matrix_mul(result, matrices[i+1])

    return result
