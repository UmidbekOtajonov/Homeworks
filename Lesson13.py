# """Task1"""
# import numpy as np
#
# a = np.arange(10, 49)
# print(a)
#
# """Task2"""
# import numpy as np
#
# # 0 dan 8 gacha bo'lgan qiymatlar
# matrix = np.arange(9).reshape(3, 3)
# print(matrix)
#
# """Task3"""
# import numpy as np
#
# # 3x3 identity matrix
# identity_matrix = np.eye(3)
# print(identity_matrix)
#
# """Task4"""
# import numpy as np
# import random
#
# # 3x3x3 array with random values
# array = np.random.rand(3, 3, 3)
# print(array)
#
# """Task5"""
# import numpy as np
# import random
#
# # 10x10 array with random values (0–1 oralig'ida)
# array = np.random.rand(10, 10)
#
# print("Array:\n", array)
#
# # Minimum va maksimum qiymatlar
# min_val = np.min(array)
# max_val = np.max(array)
#
# print("\nMinimum value:", min_val)
# print("Maximum value:", max_val)
#
# """Task6"""
# import numpy as np
# import random
# # 30 elementli tasodifiy vektor (0–1 oralig'ida)
# vector = np.random.rand(30)
#
# print("Random Vector:\n", vector)
#
# # O'rtacha qiymat
# mean_val = np.mean(vector)
# print("\nMean value:", mean_val)
#
# """Task7"""
# import numpy as np
#
# # 5x5 tasodifiy matritsa (0–100 oralig'ida butun sonlar)
# matrix = np.random.randint(0, 100, (5, 5))
# print("Original Matrix:\n", matrix)
#
# # Normalization: (x - min) / (max - min)
# normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
# print("\nNormalized Matrix:\n", normalized_matrix)
#
# """Task8"""
# import random
# import numpy as np
#
# # 5x3 matritsa (tasodifiy qiymatlar)
# A = np.random.randint(0, 10, (5, 3))
# print("Matrix A (5x3):\n", A)
#
# # 3x2 matritsa (tasodifiy qiymatlar)
# B = np.random.randint(0, 10, (3, 2))
# print("\nMatrix B (3x2):\n", B)
#
# # Real matritsa ko‘paytmasi
# C = np.dot(A, B)
# print("\nMatrix Product (5x2):\n", C)
#
#
# """Task9"""
# import numpy as np
#
# # 5x3 matritsa (tasodifiy qiymatlar)
# A = np.random.randint(0, 10, (3, 3))
# print("Matrix A (3x3):\n", A)
#
# # 3x2 matritsa (tasodifiy qiymatlar)
# B = np.random.randint(0, 10, (3, 3))
# print("\nMatrix B (3x3):\n", B)
#
# # Real matritsa ko‘paytmasi
# C = np.dot(A, B)
# print("\nMatrix Product (3 x 3):\n", C)
#
# """Task10"""
# import numpy as np
#
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix2 = matrix.transpose()
# print(matrix)
# print(matrix2)
#
# """Task11"""
#
# import numpy as np
#
# # 3x3 matritsa
# A = np.array([[2, 5, 3],
#               [1, -2, -1],
#               [3, 4, 2]])
#
# print("Matrix A:\n", A)
#
# # Determinant hisoblash
# det = np.linalg.det(A)
# print("\nDeterminant:", det)
#
# """Task12"""
#
# import numpy as np
#
# # 3x4 matritsa
# A = np.array([[1, 2, 3, 4],
#               [5, 6, 7, 8],
#               [9, 10, 11, 12]])
#
# print("Matrix A (3x4):\n", A)
#
# # 4x3 matritsa
# B = np.array([[2, 0, 1],
#               [1, 3, 2],
#               [0, 4, 5],
#               [6, 7, 8]])
#
# print("\nMatrix B (4x3):\n", B)
#
# # Matritsa ko‘paytmasi
# C = np.dot(A, B)   # yoki A @ B
# print("\nMatrix Product (A·B):\n", C)
#
#
# """Task13"""
# import numpy as np
#
# # 3x3 tasodifiy matritsa
# A = np.random.randint(0, 10, (3, 3))
# print("Matrix A (3x3):\n", A)
#
# # 3 elementli ustun vektor
# v = np.random.randint(0, 10, (3, 1))
# print("\nColumn Vector v (3x1):\n", v)
#
# # Matritsa-vektor ko‘paytmasi
# result = np.dot(A, v)   # yoki A @ v
# print("\nMatrix-Vector Product (A·v):\n", result)
#
#
# """Task14"""
# import numpy as np
#
# # Matritsa A
# A = np.array([[2, 1, -1],
#               [-3, -1, 2],
#               [-2, 1, 2]])
#
# # Vektor b
# b = np.array([8, -11, -3])
#
# # Yechim x
# x = np.linalg.solve(A, b)
# print("Solution x:", x)
#
# """Task15"""
# import numpy as np
#
# # 5x5 tasodifiy matritsa
# A = np.random.randint(0, 10, (5, 5))
# print("Matrix A:\n", A)
#
# # Qatorlar bo‘yicha yig‘indi
# row_sum = np.sum(A, axis=1)
# print("\nRow-wise sum:", row_sum)
#
# # Ustunlar bo‘yicha yig‘indi
# col_sum = np.sum(A, axis=0)
# print("Column-wise sum:", col_sum)



