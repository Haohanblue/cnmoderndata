import os
import pandas as pd
import numpy as np

# 定义标准化函数
def normalize_to_percentage(numbers):
    min_val = np.min(numbers)
    max_val = np.max(numbers)
    return round(((numbers - min_val) / (max_val - min_val)) * 100)

# 输入和输出文件夹路径
input_folder = '../../public/data/temp/03_得分计算/03_3_先直后墒/04_scores'
output_folder = '../../public/data/temp/04_百分制转换/总得分'

# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder):
    # 检查文件是否是.xlsx文件
    if file_name.endswith('.xlsx'):
        # 获取文件的完整路径
        input_file_path = os.path.join(input_folder, file_name)

        # 读取XLSX文件
        df = pd.read_excel(input_file_path)

        # 找到得分列，进行标准化
        df['得分'] = normalize_to_percentage(df['得分'])

        # 保存处理后的DataFrame到输出文件夹
        output_file_path = os.path.join(output_folder, file_name)
        df.to_excel(output_file_path, index=False)

        print(f"文件 {file_name} 已处理并保存到 {output_file_path}")