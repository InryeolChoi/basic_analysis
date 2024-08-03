# R 자료구조 정리

# 1. 벡터 (Vector)
# 벡터는 동일한 유형의 데이터 요소가 1차원 배열로 구성된 자료구조입니다.
vec_numeric <- c(1, 2, 3, 4, 5)
vec_character <- c("a", "b", "c", "d", "e")
vec_logical <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
print(vec_numeric)
print(vec_character)
print(vec_logical)

# 2. 팩터 (Factor)
# 팩터는 범주형 데이터를 다루기 위한 자료구조입니다.
factor_gender <- factor(c("Male", "Female", "Male", "Female", "Male"))
print(factor_gender)
print(levels(factor_gender))

# 3. 행렬 (Matrix)
# 행렬은 동일한 유형의 데이터 요소가 2차원 배열로 구성된 자료구조입니다.
matrix_data <- matrix(1:9, nrow = 3, ncol = 3)
print(matrix_data)

# 4. 배열 (Array)
# 배열은 행렬을 확장한 것으로, 다차원 배열로 구성된 자료구조입니다.
array_data <- array(1:24, dim = c(3, 4, 2))
print(array_data)

# 5. 데이터 프레임 (Data Frame)
# 데이터 프레임은 서로 다른 유형의 데이터 요소가 2차원 배열로 구성된 자료구조입니다.
df <- data.frame(
  ID = 1:5,
  Name = c("John", "Jane", "Paul", "Anna", "Tom"),
  Age = c(23, 25, 28, 22, 24),
  Score = c(85, 90, 88, 95, 80)
)
print(df)
print(str(df))

# 6. 리스트 (List)
# 리스트는 서로 다른 유형의 데이터 요소가 1차원 배열로 구성된 자료구조입니다.
list_data <- list(
  Name = "John",
  Age = 23,
  Scores = c(85, 90, 88),
  Passed = TRUE
)
print(list_data)
print(str(list_data))

# 7. 데이터 테이블 (Data Table)
# 데이터 테이블은 데이터 프레임보다 빠르고 효율적으로 데이터를 처리할 수 있는 자료구조입니다.
# 데이터 테이블을 사용하려면 data.table 패키지를 설치해야 합니다.
# install.packages("data.table")
library(data.table)
dt <- data.table(
  ID = 1:5,
  Name = c("John", "Jane", "Paul", "Anna", "Tom"),
  Age = c(23, 25, 28, 22, 24),
  Score = c(85, 90, 88, 95, 80)
)
print(dt)
print(str(dt))

# 각 자료구조의 장단점과 사용 예시
# - 벡터: 빠르고 효율적이지만 동일한 유형의 데이터만 저장할 수 있습니다.
# - 팩터: 범주형 데이터를 다룰 때 유용합니다.
# - 행렬: 동일한 유형의 데이터를 2차원 배열로 저장할 때 사용합니다.
# - 배열: 다차원 배열 데이터를 저장할 때 사용합니다.
# - 데이터 프레임: 서로 다른 유형의 데이터를 2차원 배열로 저장할 때 유용합니다.
# - 리스트: 서로 다른 유형의 데이터를 1차원 배열로 저장할 때 유용합니다.
# - 데이터 테이블: 대용량 데이터를 효율적으로 처리할 때 유용합니다.

# End of Script