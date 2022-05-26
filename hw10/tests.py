import unittest
import time
from python_matrix_mul import python_chain_matrix_mul
import numpy as np
import cython_realization


class TestChainMatrixMul(unittest.TestCase):
    def test_mul_two_matrix(self):
        a_matrix = [[3, 1, 2], [0, 2, 3], [1, 1, 1]]
        b_matrix = [[4, 2, 1], [1, 2, 8], [3, 2, 1]]

        numpy_result = np.matmul(a_matrix, b_matrix)
        python_result = python_chain_matrix_mul([a_matrix, b_matrix])
        cython_result = cython_realization.cython_chain_matrix_mul([a_matrix, b_matrix])

        self.assertTrue((numpy_result == python_result).all())
        self.assertTrue((numpy_result == cython_result).all())

    def test_mul_multiple_matrix(self):
        matrices = [[[i+j+k for i in range(5)] for j in range(5)] for k in range(5)]

        numpy_matrices = np.array(matrices)
        numpy_result = numpy_matrices[0]
        for i in range(4):
            numpy_result = np.matmul(numpy_result, numpy_matrices[i+1])

        python_result = python_chain_matrix_mul(matrices)
        cython_result = cython_realization.cython_chain_matrix_mul(matrices)

        self.assertTrue((numpy_result == python_result).all())
        self.assertTrue((numpy_result == cython_result).all())

    def test_mul_different_dim(self):
        a_matrix = [[1, 2], [3, 4]]
        b_matrix = [[1, 3, 5, 7], [1, 2, 3, 4]]
        c_matrix = [[2, 1], [3, 8], [2, 2], [1, 1]]

        numpy_result = np.matmul(np.matmul(a_matrix, b_matrix), c_matrix)
        python_result = python_chain_matrix_mul([a_matrix, b_matrix, c_matrix])
        cython_result = cython_realization.cython_chain_matrix_mul([a_matrix, b_matrix, c_matrix])

        self.assertTrue((numpy_result == python_result).all())
        self.assertTrue((numpy_result == cython_result).all())

    def test_time(self):
        matrices = [[[i * 3 + j for i in range(90)] for j in range(90)] for k in range(60)]

        start_ts = time.time()

        python_chain_matrix_mul(matrices)

        end_ts = time.time()
        print(f'Python time: {end_ts - start_ts}')

        start_ts = time.time()

        cython_realization.cython_chain_matrix_mul(matrices)

        end_ts = time.time()
        print(f'Cython time: {end_ts - start_ts}')


if __name__ == '__main__':
    unittest.main()
