import numpy as np

random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 matrix:\n", random_matrix)

matrix_sum = np.sum(random_matrix)
print(f"\nSum of all elements: {matrix_sum}")

matrix_mean = np.mean(random_matrix)
print(f"\nMean of the matrix: {matrix_mean:2.2f}")

transpose_matrix = np.transpose(random_matrix)
print(f"\nTranspose Matrix:\n{transpose_matrix}")
