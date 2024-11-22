from Compiler import library

def secure_strassen(A, B, n):
    if n <= 2:
        return secure_dot_product(A, B)
    
    mid = n // 2
    A11, A12, A21, A22 = split_matrix_securely(A, mid)
    B11, B12, B21, B22 = split_matrix_securely(B, mid)

    # Secure recursive calls
    P1 = secure_strassen(A11, B12 - B22, mid)
    P2 = secure_strassen(A11 + A12, B22, mid)
    P3 = secure_strassen(A21 + A22, B11, mid)
    P4 = secure_strassen(A22, B21 - B11, mid)
    P5 = secure_strassen(A11 + A22, B11 + B22, mid)
    P6 = secure_strassen(A12 - A22, B21 + B22, mid)
    P7 = secure_strassen(A11 - A21, B11 + B12, mid)

    # Combine results
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    return combine_matrices_securely(C11, C12, C21, C22)


