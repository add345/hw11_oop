#Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

class Matrix:

     def __init__(self, matr):
         self._matr = matr

     def get_matrix(self):
         return self._matr
     
     def __eq__(self, other):
         if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
         else:
             for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                   if self._matr[i][j] != other._matr[i][j]:
                         return False
                         return True

     def __add__(self, other):
         if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
             return f'Error: матрицы разных размеров'
         else:
             return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

     def __mul__(self, other):
         if len(self._matr) != len(other._matr):
             return f'Error: невозможно перемножить матрицы'
         else:
             new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
             return Matrix(new_matr)

     def __eq__(self, other):
         if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            return f'Error: матрицы разных размеров'
         else:
             for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                   if self._matr[i][j] != other._matr[i][j]:
                         return False
                         return True
      
     def __str__(self):
         s = ''
         for i in range(len(self._matr)):
             s += str(self._matr[i]) + '\n'
         return s

a1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
a2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
a3 = [1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]
a4 = [1, 2, 4], [5, 6,  8], [2, 5, -2]


m_1 = Matrix(a1)
m_2 = Matrix(a2)
m_3 = Matrix(a3)
m_4 = Matrix(a4)

print ("Cравнение матриц:")

print(m_1 == m_1)
print(m_1 == m_2)

print ("Cложение матриц:")
matrix_sum = m_1 + m_2
print(matrix_sum)

print ("Умножение матриц:")
matrix_mul = m_1 * m_3
print(matrix_mul)
print(m_1 * m_4)

