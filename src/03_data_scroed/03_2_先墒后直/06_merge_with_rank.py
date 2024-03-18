import os
import pandas as pd

# 定义文件夹路径
folder_path = '../../../public/data/temp/03_得分计算/03_2_先墒后直/05_分项得分'

# 读取文件夹中所有.xlsx文件的路径和文件名
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 定义一个空的DataFrame用于存储合并后的数据
merged_df = pd.DataFrame()

# 读取第一个文件的前两列数据
first_file = pd.read_excel(file_paths[0])
first_two_cols = first_file.iloc[:, :2]

# 将第一个文件的前两列数据添加到合并后的DataFrame的前两列
merged_df[first_two_cols.columns[0]] = first_two_cols.iloc[:, 0]
merged_df[first_two_cols.columns[1]] = first_two_cols.iloc[:, 1]

# 逐个读取文件并将第三列和第四列数据合并到DataFrame中
for idx, file_path in enumerate(file_paths):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 获取第三列和第四列数据
    col_3_data = df.iloc[:, 2]  # 选择第三列，索引从0开始
    col_4_data = df.iloc[:, 3]  # 选择第四列，索引从0开始

    # 将第三列和第四列数据添加到DataFrame中，并使用文件的原始列名作为列名
    col3_name = df.columns[2]  # 获取第三列的原始列名
    merged_df[col3_name] = col_3_data

    # 新列名按顺序命名
    rank_col_name = f"{chr(ord('A') + idx)}排名"
    merged_df[rank_col_name] = col_4_data

# 计算总得分并复制数据以备分组计算总得分排名
merged_df['总得分'] = merged_df[['A', 'B', 'C', 'D', 'E']].mean(axis=1)
merged_df_copy = merged_df.copy()  # 复制数据以备分组计算排名

# 按年份分组计算总得分排名
merged_df_copy['时间'] = merged_df_copy['时间']  # 假设时间列为‘时间’
yearly_ranking = merged_df_copy.groupby('时间')['总得分'].rank(method='min', ascending=False)

# 将年份和对应的排名填入复制后的DataFrame中
merged_df_copy['总得分排名'] = yearly_ranking.astype(int)

# 保存合并后的数据到新文件
merged_file_path = '../../../public/data/temp/03_得分计算/03_2_先墒后直/合并数据_排名.xlsx'
merged_df_copy.to_excel(merged_file_path, index=False, engine='openpyxl')
if not os.path.exists('../../../public/data/result/'):
    os.makedirs('../../../public/data/result/')
merged_file_path_2 = '../../../public/data/result/方法2得分.xlsx'
merged_df_copy.to_excel(merged_file_path_2, index=False, engine='openpyxl')

print(f'合并后的数据已保存到文件: {merged_file_path} 和 {merged_file_path_2}')
