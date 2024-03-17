import os
import pandas as pd
import numpy as np

# 定义计算-k的函数
def calculate_k(column):
    non_zero_count = column.astype(bool).sum()  # 非零元素的数量
    k = 1 / np.log(non_zero_count) if non_zero_count > 1 else 0  # 根据公式计算-k，避免除以零
    return k

# 定义计算熵值的函数
def calculate_entropy(column):
    sum_x = column.sum()  # 第三列开始的所有值的总和
    k = calculate_k(column)
    if k == 0:
        return 0
    y = column / sum_x  # 计算 y_ij
    y = y.replace(0, np.nan)  # 将 0 替换为 NaN，避免 log(0) 的情况
    entropy = -k * np.sum(y * np.log(y))  # 计算熵值，乘以-k
    return entropy

base_fileinput = "../../../public/data/temp/03_得分计算/03_2_先墒后直/01_标准化数据"
base_file_output = "../../../public/data/temp/03_得分计算/03_2_先墒后直/02_y_ij_entropy/"

# 处理每个文件夹
for folder_name in os.listdir(base_fileinput):
    input_folder = os.path.join(base_fileinput, folder_name)
    output_folder = os.path.join(base_file_output, folder_name)
    os.makedirs(output_folder, exist_ok=True)

    # 处理每个 Excel 文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xlsx'):
            input_file_path = os.path.join(input_folder, file_name)
            new_filename = file_name.replace("normalized", "")
            y_ij_file_path = os.path.join(output_folder, f'y_ij_entropy_{new_filename}')

            # 读取 Excel 文件
            df = pd.read_excel(input_file_path)

            # 从第三列开始计算熵值并存储到新列中
            entropy_values = df.iloc[:, 2:].apply(calculate_entropy, axis=0)

            # 将结果添加到新的 DataFrame 中
            entropy_df = pd.DataFrame({'Entropy': entropy_values})

            # 将 y_ij 数据保存到第一个工作表中
            df_with_y_ij = df.copy()
            df_with_y_ij.iloc[:, 2:] = df_with_y_ij.iloc[:, 2:] / df_with_y_ij.iloc[:, 2:].sum(axis=0)

            # 将结果保存到新的 Excel 文件中
            with pd.ExcelWriter(y_ij_file_path) as writer:
                df_with_y_ij.to_excel(writer, index=False, sheet_name='Sheet1')  # 写入第一个工作表

                # 创建第二个工作表并写入熵值
                entropy_df.to_excel(writer, index=False, sheet_name='Sheet2')

print("熵值计算并保存完成。")
