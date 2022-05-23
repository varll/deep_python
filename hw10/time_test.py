import time
import cython_realization
from python_matrix_mul import python_chain_matrix_mul

if __name__ == '__main__':
    matrices = [[[i*3 + j for i in range(90)] for j in range(90)] for k in range(60)]

    start_ts = time.time()

    python_chain_matrix_mul(matrices)

    end_ts = time.time()
    print(f'Python time: {end_ts - start_ts}')

    start_ts = time.time()

    cython_realization.cython_chain_matrix_mul(matrices)

    end_ts = time.time()
    print(f'Cython time: {end_ts - start_ts}')
