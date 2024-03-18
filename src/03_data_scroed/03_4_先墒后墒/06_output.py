import pandas as pd
import os
# 读取合并数据文件和方法4总得分文件
file1_path = '../../../public/data/temp/03_得分计算/03_2_先墒后直/合并数据_排名.xlsx'
file2_path = '../../../public/data/temp/03_得分计算/03_4_先墒后墒/04_合并得分数据.xlsx'
if not os.path.exists('../../../public/data/result'):
    os.makedirs('../../../public/data/result')
# 读取文件内容
df1 = pd.read_excel(file1_path,usecols=lambda x: x not in ['总得分', '总得分排名'])
df2 = pd.read_excel(file2_path)

# 合并数据
merged_df = pd.merge(df1, df2, on=['省份', '时间'], how='inner')

# 保存合并后的数据到新文件
merged_file_path = '../../../public/data/result/方法4得分.xlsx'
merged_df.to_excel(merged_file_path, index=False, engine='openpyxl')

print(f'合并后的数据已保存到文件: {merged_file_path}')
