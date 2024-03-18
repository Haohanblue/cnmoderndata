import numpy as np

# 假设我们有以下一串数字
numbers = np.array([10, 20, 30, 40, 50])

# 找到最大值和最小值
min_val = np.min(numbers)
max_val = np.max(numbers)

# 按比例标准化为百分制
normalized_numbers = ((numbers - min_val) / (max_val - min_val)) * 100

print(normalized_numbers)