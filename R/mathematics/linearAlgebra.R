# 선형대수의 모든 연산을 담은 R 코드

# 벡터 연산
v1 <- c(1, 2, 3)
v2 <- c(4, 5, 6)

# 벡터 덧셈
v_add <- v1 + v2
print("Vector Addition:")
print(v_add)

# 벡터 상수배
v_scalar_mult <- 2 * v1
print("Scalar Multiplication of Vector:")
print(v_scalar_mult)

# 벡터 내적
v_inner <- sum(v1 * v2)
print("Inner Product of Vectors:")
print(v_inner)

# 벡터 외적
v_outer <- outer(v1, v2)
print("Outer Product of Vectors:")
print(v_outer)

# Hadamard Product
v_hadamard <- v1 * v2
print("Hadamard Product of Vectors:")
print(v_hadamard)

# Kronecker Product
v_kronecker <- kronecker(v1, v2)
print("Kronecker Product of Vectors:")
print(v_kronecker)

# 행렬 연산
m1 <- matrix(1:4, nrow = 2, ncol = 2)
m2 <- matrix(5:8, nrow = 2, ncol = 2)

# 행렬 덧셈
m_add <- m1 + m2
print("Matrix Addition:")
print(m_add)

# 행렬 곱셈
m_mult <- m1 %*% m2
print("Matrix Multiplication:")
print(m_mult)

# 행렬 상수배
m_scalar_mult <- 2 * m1
print("Scalar Multiplication of Matrix:")
print(m_scalar_mult)

# 행렬의 전치
m_transpose <- t(m1)
print("Transpose of Matrix:")
print(m_transpose)

# 행렬의 역행렬
m_inverse <- solve(m1)
print("Inverse of Matrix:")
print(m_inverse)

# 행렬의 랭크
m_rank <- qr(m1)$rank
print("Rank of Matrix:")
print(m_rank)

# 유사역행렬 (Moore-Penrose Pseudoinverse)
m_pseudoinverse <- MASS::ginv(m1)
print("Moore-Penrose Pseudoinverse of Matrix:")
print(m_pseudoinverse)

# 고유값과 고유벡터
eig <- eigen(m1)
print("Eigenvalues of Matrix:")
print(eig$values)
print("Eigenvectors of Matrix:")
print(eig$vectors)

# 행렬의 대각화
eig_D <- diag(eig$values)
eig_P <- eig$vectors
print("Diagonal Matrix from Eigenvalues:")
print(eig_D)
print("Matrix of Eigenvectors:")
print(eig_P)

# 행렬의 대각화 확인 (A = PDP^-1)
m_diagonalized <- eig_P %*% eig_D %*% solve(eig_P)
print("Diagonalized Matrix:")
print(m_diagonalized)

# 행렬의 Hadamard Product
m_hadamard <- m1 * m2
print("Hadamard Product of Matrices:")
print(m_hadamard)

# 행렬의 Kronecker Product
m_kronecker <- kronecker(m1, m2)
print("Kronecker Product of Matrices:")
print(m_kronecker)

# 행렬의 Direct Sum
direct_sum <- function(A, B) {
  matrix(c(A, matrix(0, nrow(A), ncol(B)), matrix(0, nrow(B), ncol(A)), B), 
         nrow = nrow(A) + nrow(B), ncol = ncol(A) + ncol(B))
}
m_direct_sum <- direct_sum(m1, m2)
print("Direct Sum of Matrices:")
print(m_direct_sum)

# 행렬의 Tensor Product
tensor_product <- function(A, B) {
  array(A %o% B, dim = c(dim(A), dim(B)))
}
m_tensor_product <- tensor_product(m1, m2)
print("Tensor Product of Matrices:")
print(m_tensor_product)

# 선형방정식의 해
A <- matrix(c(2, -1, 0, -1, 2, -1, 0, -1, 2), nrow = 3, byrow = TRUE)
b <- c(1, 0, 1)
x <- solve(A, b)
print("Solution to Linear System Ax = b:")
print(x)

# QR 분해
qr_decomp <- qr(m1)
Q <- qr.Q(qr_decomp)
R <- qr.R(qr_decomp)
print("QR Decomposition - Q Matrix:")
print(Q)
print("QR Decomposition - R Matrix:")
print(R)

# SVD 분해
svd_decomp <- svd(m1)
U <- svd_decomp$u
D <- diag(svd_decomp$d)
V <- svd_decomp$v
print("SVD Decomposition - U Matrix:")
print(U)
print("SVD Decomposition - D Matrix:")
print(D)
print("SVD Decomposition - V Matrix:")
print(V)

# Gram-Schmidt 직교화
gram_schmidt <- function(X) {
  n <- ncol(X)
  Q <- matrix(0, nrow(X), n)
  for (i in 1:n) {
    v <- X[, i]
    for (j in 1:(i-1)) {
      r <- sum(Q[, j] * X[, i])
      v <- v - r * Q[, j]
    }
    Q[, i] <- v / sqrt(sum(v^2))
  }
  return(Q)
}
m_gram_schmidt <- gram_schmidt(m1)
print("Gram-Schmidt Orthogonalization:")
print(m_gram_schmidt)

# 행렬식
m_det <- det(m1)
print("Determinant of Matrix:")
print(m_det)

# 행렬의 Trace
m_trace <- sum(diag(m1))
print("Trace of Matrix:")
print(m_trace)