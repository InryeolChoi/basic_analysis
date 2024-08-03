# apply, lapply, sapply, tapply, mapply 함수 정리

# 1. apply
# 행렬 또는 데이터 프레임에 함수 적용
matrix_data <- matrix(1:9, nrow = 3, ncol = 3)
print("Original Matrix:")
print(matrix_data)

# 각 행의 합 계산
row_sums <- apply(matrix_data, 1, sum)
print("Row Sums:")
print(row_sums)

# 각 열의 평균 계산
col_means <- apply(matrix_data, 2, mean)
print("Column Means:")
print(col_means)

# 예제: 행렬의 각 요소에 제곱근 함수 적용
sqrt_matrix <- apply(matrix_data, c(1, 2), sqrt)
print("Square Roots of Matrix Elements:")
print(sqrt_matrix)


# 2. lapply
# 리스트 또는 벡터에 함수 적용, 리스트로 반환
list_data <- list(a = 1:5, b = 6:10, c = 11:15)
print("Original List:")
print(list_data)

# 각 리스트 요소의 합 계산
list_sums <- lapply(list_data, sum)
print("List Sums:")
print(list_sums)

# 예제: 리스트의 각 요소에 제곱 함수 적용
list_squared <- lapply(list_data, function(x) x^2)
print("List Squared:")
print(list_squared)

# 3. sapply
# 리스트 또는 벡터에 함수 적용, 벡터 또는 행렬로 반환
# lapply와 동일한 작업을 수행하지만 결과를 벡터 또는 행렬로 반환
list_sums_s <- sapply(list_data, sum)
print("List Sums with sapply:")
print(list_sums_s)

# 각 리스트 요소의 평균 계산
list_means <- sapply(list_data, mean)
print("List Means:")
print(list_means)

# 예제: 리스트의 각 요소에 로그 함수 적용
list_log <- sapply(list_data, log)
print("List Logarithms:")
print(list_log)

# 4. tapply
# 벡터에 함수 적용, 그룹별로 계산
# 그룹화된 벡터의 평균 계산
vector_data <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
groups <- gl(2, 5)
print("Original Vector:")
print(vector_data)
print("Groups:")
print(groups)

group_means <- tapply(vector_data, groups, mean)
print("Group Means:")
print(group_means)

# 예제: 그룹화된 벡터의 합 계산
group_sums <- tapply(vector_data, groups, sum)
print("Group Sums:")
print(group_sums)

# 예제: 그룹화된 벡터의 표준 편차 계산
group_sds <- tapply(vector_data, groups, sd)
print("Group Standard Deviations:")
print(group_sds)

# 5. mapply
# 여러 리스트 또는 벡터에 함수 적용, 대응되는 요소에 함수 적용
# 두 벡터의 합 계산
vector1 <- 1:5
vector2 <- 6:10
print("Vector 1:")
print(vector1)
print("Vector 2:")
print(vector2)

vector_sums <- mapply(sum, vector1, vector2)
print("Element-wise Sums with mapply:")
print(vector_sums)

# 예제: 두 벡터의 곱 계산
vector_products <- mapply(function(x, y) x * y, vector1, vector2)
print("Element-wise Products with mapply:")
print(vector_products)

# 예제: 두 벡터의 차이 계산
vector_diffs <- mapply(function(x, y) x - y, vector1, vector2)
print("Element-wise Differences with mapply:")
print(vector_diffs)

# 예제: 세 벡터의 합 계산
vector3 <- 11:15
vector_sums2 <- mapply(sum, vector1, vector2, vector3)
print("Element-wise Sums with Three Vectors:")
print(vector_sums2)

# End of Script