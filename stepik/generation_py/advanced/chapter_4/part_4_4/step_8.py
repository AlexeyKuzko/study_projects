"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 4 / Step 8."""

# Считываем количество строк и столбцов
n = int(input())
m = int(input())

# Считываем элементы матрицы
matrix = [input() for _ in range(n * m)]

# Выводим матрицу
for i in range(n):
    print(" ".join(matrix[i * m : (i + 1) * m]))
