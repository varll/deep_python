cpdef cython_matrix_mul(list a_matrix, list b_matrix):
    cdef int rows_a = len(a_matrix)
    cdef int cols_a = len(a_matrix[0])
    cdef int cols_b = len(b_matrix[0])

    cdef list c_matrix
    c_matrix = [[0 for col in range(cols_b)] for row in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]

    return c_matrix


cpdef cython_chain_matrix_mul(list matrices):
    cdef list result = matrices[0]
    for i in range(len(matrices)-1):
        result = cython_matrix_mul(result, matrices[i+1])

    return result