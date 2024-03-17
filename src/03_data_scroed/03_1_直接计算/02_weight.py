import os
import pandas as pd

# 定义计算权重的函数
def calculate_weights(ej_values):
    denominator = (1 - ej_values).sum()
    weights = (1 - ej_values) / denominator
    return weights

# 设置输入和输出文件夹路径
input_folder = '../../../public/data/temp/03_得分计算/03_1_直接计算/01_y_ij_entropy'
output_folder = '../../../public/data/temp/03_得分计算/03_1_直接计算/02_weighted_y_ij_entropy'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 处理每个 Excel 文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, f'weighted_{file_name}')

        # 读取 Excel 文件的第一个工作表(sheet)
        with pd.ExcelFile(input_file_path) as xls:
            sheet1_df = pd.read_excel(xls, sheet_name='Sheet1')

        # 读取 Excel 文件的第二个工作表(sheet)
        with pd.ExcelFile(input_file_path) as xls:
            sheet2_df = pd.read_excel(xls, sheet_name='Sheet2')

        # 提取ej列的值
        ej_values = sheet2_df['Entropy'].values

        # 计算权重
        weights = calculate_weights(ej_values)

        # 将权重添加到第二个工作表(sheet)中
        sheet2_df['Weights'] = weights

        # 将原始数据第一个工作表(sheet)和带有权重的第二个工作表(sheet)写入到新的 Excel 文件中
        with pd.ExcelWriter(output_file_path) as writer:
            sheet1_df.to_excel(writer, index=False, sheet_name='Sheet1')
            sheet2_df.to_excel(writer, index=False, sheet_name='Sheet2')

print("权重计算并保存完成。")
