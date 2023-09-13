import random
def matrix_gen():
    m=random.randint(2, 11)
    n=random.randint(2, 11)
    #print(m, n)
    matrix=[]
    for i in range(m):
        matrix.append([])
        for _ in range(n):
            matrix[i].append(random.randint(-100, 100))
            
    return matrix

def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:4}', end=' ')
        print()
    
def matrix_transp(matrix):
    res=[]
    for j in range(len(matrix[0])):
        res.append([])
        for i in range(len(matrix)):
            res[j].append(matrix[i][j])
    return res

matr=matrix_gen()
print('Исходная матрица')
matrix_print(matr)
matr=matrix_transp(matr)
print('Транспонированная матрица')
matrix_print(matr)