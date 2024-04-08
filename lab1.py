
# T(n) = 3n + 1
# min(n) = T(n)
# max(n) = T(n)
def scalar_product(vector1, vector2):
    n = len(vector1)
    result = 0  # 1
    for i in range(n):
        result += vector1[i] * vector2[i]  # 3
    
    print(result) 


# T(n) = 3n^3 + 1
# min(n) = T(n)
# max(n) = T(n)
def matrix_multiplication(matrix1, matrix2):
    n = len(matrix1)
    result = [[0]*n]*n  # 1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # 3
    
    print(result)


# T(n) = (n-1)(2+n/2+1)/2 + (n-1)(2+3n/2+4)/2 = (n-1)(n+4.5)    T(2) = 6.5
# min(n) = (n-1)(2+n/2+1)
# max(n) = (n-1)(2+3n/2+4)
def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        m = a[i]  # 1
        p = i  # 1
        for j in range(i+1, n):
            if m > a[j]:  # 1
                m = a[j]  # 1
                p = j  # 1
        
        if p != i:  # 1
            a[i], a[p] = a[p], a[i]  # 3
    
    print(a)


# T(n) = (n-1)((n-1)/2*4) = 2(n-1)^2    T(2) = 2
# min(n) = 2(n-1)
# max(n) = 4(n-1)^2
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):  # n-1
        for j in range(i, 0, -1):  # n-1
            if a[j] < a[j-1]:  # 1
                a[j], a[j-1] = a[j-1], a[j]  # 3
            else:
                break # 1
    
    print(a)


# T(n) = (n-1)n/4 + 2(n-1)n/2 = 5n(n-1)/4    T(2) = 2.5
# max(n) = (n-1)(n/2 * 4) = 2(n-1)n
# min(n) = (n-1)n/2
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:  # 1
                a[j], a[j+1] = a[j+1], a[j]  # 3
    
    print(a)