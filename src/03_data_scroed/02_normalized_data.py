
import os
import pandas as pd

# 读取文件夹中的所有xlsx文件
folder_path = '../../public/data/temp/03_得分计算/01_时间数据'
output_folder = '../../public/data/temp/03_得分计算/02_标准化数据'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)

        # 读取Excel文件
        df = pd.read_excel(file_path)

        # 将数据列转换为数值类型
        df.iloc[:, 2:] = df.iloc[:, 2:].apply(pd.to_numeric, errors='coerce')

        # 保存正负号属性到数组
        attributes = ['+', '-', '+', '+', '-', '+', '-', '+', '-', '-', '-', '-', '-', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+','+', '-', '+', '+','+', '-', '+', '+','+', '+', '+','+', '+','+']

        # 定义标准化函数
        def normalize_column(column, attribute):
            min_val = column.min()
            max_val = column.max()
            if attribute == '+':
                return (column - min_val) / (max_val - min_val)
            elif attribute == '-':
                return (max_val - column) / (max_val - min_val)
            else:
                return column

        # 对每列应用标准化函数
        for col, attr in zip(df.columns[2:], attributes):  # 从第二列开始
            df[col] = normalize_column(df[col], attr)

        # 保存结果到新的Excel文件
        output_file_path = os.path.join(output_folder, f'normalized_{file_name}')
        df.to_excel(output_file_path, index=False)

print("处理完成。")
