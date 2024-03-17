import os
import pandas as pd

# 设置输入和输出文件夹路径
input_folder = '../../../public/data/temp/03_得分计算/03_1_直接计算/02_weighted_y_ij_entropy'
output_folder = '../../../public/data/temp/03_得分计算/03_1_直接计算/03_scores'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 处理每个 Excel 文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, f'scores_{file_name[-10:]}')

        # 读取 Excel 文件的第一个工作表(sheet)中的数据作为y_ij和省份信息
        with pd.ExcelFile(input_file_path) as xls:
            sheet1_df = pd.read_excel(xls, sheet_name='Sheet1')

        # 读取 Excel 文件的第二个工作表(sheet)中的数据作为weights
        with pd.ExcelFile(input_file_path) as xls:
            sheet2_df = pd.read_excel(xls, sheet_name='Sheet2')

        # 提取y_ij和weights列的数据，并将 NaN 值填充为 0
        y_ij = sheet1_df.iloc[:, 2:].fillna(0).values
        weights = sheet2_df['Weights'].fillna(0).values

        # 计算每个指标的得分
        scores = y_ij.dot(weights)

        # 创建包含得分和省份信息的DataFrame
        scores_df = pd.DataFrame({'省份': sheet1_df.iloc[:, 0], '得分': scores})

        # 添加排名列
        scores_df['排名'] = scores_df['得分'].rank(ascending=False)

        # 将结果保存到新的 Excel 文件中
        scores_df.to_excel(output_file_path, index=False)

print("得分计算并保存完成。")
