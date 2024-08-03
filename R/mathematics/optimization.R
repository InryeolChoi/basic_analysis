# 최적화 이론의 다양한 내용을 담은 R 코드

# 필요한 패키지 설치 및 로드
install.packages("lpSolve")
install.packages("quadprog")
install.packages("Rsolnp")
install.packages("optimx")
install.packages("nloptr")
library(lpSolve)
library(quadprog)
library(Rsolnp)
library(optimx)
library(nloptr)

# 1. 선형 최적화 (Linear Programming)
# 예제: 최대화 문제
# max z = 3x + 2y
# subject to:
# 2x + y <= 20
# 4x - 5y >= -10
# -x + 2y <= 15
# x, y >= 0

obj <- c(3, 2)  # Objective function coefficients
con <- matrix(c(2, 1, 4, -5, -1, 2), nrow = 3, byrow = TRUE)  # Constraints
dir <- c("<=", ">=", "<=")  # Direction of constraints
rhs <- c(20, -10, 15)  # Right-hand side of constraints

# 선형 최적화 문제 풀기
lp_result <- lp("max", obj, con, dir, rhs, compute.sens = TRUE)
print("Linear Programming Result:")
print(lp_result)

# 2. 이차 최적화 (Quadratic Programming)
# 예제: 최소화 문제
# min 1/2 x^T D x - d^T x
# subject to:
# A x >= b

D <- matrix(c(1, 0, 0, 1), nrow = 2)  # Quadratic term
d <- c(-4, -6)  # Linear term
A <- matrix(c(1, 1, -1, 2, 2, 1), nrow = 3, byrow = TRUE)  # Constraints
b <- c(2, 2, 3)  # Right-hand side of constraints

# 이차 최적화 문제 풀기
qp_result <- solve.QP(D, d, t(A), b)
print("Quadratic Programming Result:")
print(qp_result$solution)

# 3. 비선형 최적화 (Nonlinear Programming)
# 예제: Rosenbrock 함수 최소화
# min f(x, y) = 100(y - x^2)^2 + (1 - x)^2

rosenbrock <- function(x) {
  return(100 * (x[2] - x[1]^2)^2 + (1 - x[1])^2)
}

# 비선형 최적화 문제 풀기
nl_result <- optim(c(-1.2, 1), rosenbrock)
print("Nonlinear Programming Result:")
print(nl_result$par)

# 4. 제약 조건이 있는 최적화 (Constrained Optimization)
# 예제: Equality and inequality constraints
# min f(x) = (x[1] - 1)^2 + (x[2] - 2.5)^2
# subject to:
# g1(x) = x[1] - 2 * x[2] + 2 <= 0
# g2(x) = x[1]^2 + x[2]^2 <= 2
# h(x) = x[1] + x[2] = 2

obj_fn <- function(x) {
  return((x[1] - 1)^2 + (x[2] - 2.5)^2)
}

ineq_con <- function(x) {
  return(c(x[1] - 2 * x[2] + 2, x[1]^2 + x[2]^2 - 2))
}

eq_con <- function(x) {
  return(x[1] + x[2] - 2)
}

# 제약 조건이 있는 최적화 문제 풀기
con_result <- solnp(c(1, 1), obj_fn, eqfun = eq_con, eqB = 0, ineqfun = ineq_con, ineqLB = c(-Inf, -Inf), ineqUB = c(0, 0))
print("Constrained Optimization Result:")
print(con_result$pars)

# 5. 글로벌 최적화 (Global Optimization)
# 예제: Simulated Annealing을 이용한 최적화
# min f(x) = (x - 2)^2

global_obj <- function(x) {
  return((x - 2)^2)
}

# 글로벌 최적화 문제 풀기
global_result <- optimx(par = 10, fn = global_obj, method = "SANN")
print("Global Optimization Result:")
print(global_result)

# 6. 다변수 제약 조건이 있는 최적화 (Multivariable Constrained Optimization)
# 예제: nloptr 패키지를 이용한 최적화
# min f(x, y) = (x - 2)^2 + (y - 2)^2
# subject to:
# x + y <= 3
# x >= 0
# y >= 0

multivar_obj <- function(x) {
  return((x[1] - 2)^2 + (x[2] - 2)^2)
}

multivar_con <- function(x) {
  return(c(x[1] + x[2] - 3, -x[1], -x[2]))
}

# 다변수 제약 조건이 있는 최적화 문제 풀기
multivar_result <- nloptr(x0 = c(1, 1), eval_f = multivar_obj, lb = c(0, 0), ub = c(Inf, Inf), eval_g_ineq = multivar_con, opts = list(algorithm = "NLOPT_LN_COBYLA", xtol_rel = 1.0e-8))
print("Multivariable Constrained Optimization Result:")
print(multivar_result$solution)