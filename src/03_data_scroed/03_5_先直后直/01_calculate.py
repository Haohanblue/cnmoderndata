import os
import pandas as pd

# 定义文件夹路径
folder_path = '../../../public/data/temp/03_得分计算/03_4_先墒后墒/02_标准化数据'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if not os.path.exists('../../../public/data/temp/03_得分计算/03_5_先直后直/'):
    os.makedirs('../../../public/data/temp/03_得分计算/03_5_先直后直/')
# 读取文件夹中所有.xlsx文件的路径和文件名
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 定义一个空的DataFrame用于存储合并后的数据
merged_df = pd.DataFrame()

# 逐个读取文件并计算总得分和排名
for file_path in file_paths:
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 计算总得分
    df['总得分'] = df[['A', 'B', 'C', 'D', 'E']].mean(axis=1)

    # 计算总得分排名
    df['总得分排名'] = df['总得分'].rank(method='min', ascending=False)

    # 添加到合并后的DataFrame中
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# 保存合并后的数据到新文件
merged_file_path = '../../../public/data/temp/03_得分计算/03_5_先直后直/合并数据_排名.xlsx'
merged_df.to_excel(merged_file_path, index=False, engine='openpyxl')

merged_file_path_2 = '../../../public/data/result/方法5得分.xlsx'
merged_df.to_excel(merged_file_path_2, index=False, engine='openpyxl')
print(f'合并后的数据已保存到文件: {merged_file_path}和{merged_file_path_2}')
