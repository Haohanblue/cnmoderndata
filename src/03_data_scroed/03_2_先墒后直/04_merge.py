import os
import pandas as pd

# 设置输入和输出文件夹路径
input_base_folder = '../../../public/data/temp/03_得分计算/03_2_先墒后直/03_weights_entropy'
output_base_folder = '../../../public/data/temp/03_得分计算/03_2_先墒后直/05_分项得分'

# 处理每个文件夹
for folder_name in os.listdir(input_base_folder):
    input_folder = os.path.join(input_base_folder, folder_name)
    output_file = os.path.join(output_base_folder, f'分项得分_{folder_name}.xlsx')

    # 创建一个空的 DataFrame 用于存储所有年份的得分数据
    combined_scores_df = pd.DataFrame(columns=['省份', '时间', f'{folder_name}'])

    # 处理每个 Excel 文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.xlsx'):
            year = int(file_name.split("_")[4])  # 从文件名中提取年份
            input_file_path = os.path.join(input_folder, file_name)

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

            # 创建包含得分和省份信息的 DataFrame
            year_scores_df = pd.DataFrame({'省份': sheet1_df.iloc[:, 0], '时间': year, f'{folder_name}': scores})

            # 将该年份的得分数据添加到 combined_scores_df 中
            combined_scores_df = pd.concat([combined_scores_df, year_scores_df])

    # 按时间和得分排序
    combined_scores_df.sort_values(by=['时间'], ascending=[True], inplace=True)

    # 计算排名并添加到 DataFrame 中
    combined_scores_df['排名'] = combined_scores_df.groupby('时间')[f'{folder_name}'].rank(ascending=False, method='min')

    # 将结果保存到新的 Excel 文件中
    combined_scores_df.to_excel(output_file, index=False)

print("得分计算并保存完成。")
