import pandas as pd

# 读取两个.xlsx文件
df1 = pd.read_excel('../../public/data/temp/04_百分制转换/分项数据.xlsx')
df2 = pd.read_excel('../../public/data/temp/04_百分制转换/总得分.xlsx')

# 以'省份'和'时间'两列作为键，合并两个DataFrame
merged_df = pd.merge(df1, df2, on=['省份', '时间'])

# 定义新的列顺序
new_order = ['省份', '时间', 'A', 'B', 'C', 'D', 'E', '得分','排名', 'A排名', 'B排名', 'C排名', 'D排名', 'E排名']

# 改变列的顺序
merged_df = merged_df.reindex(columns=new_order)
merged_df = merged_df.rename(columns={'得分': 'score'})
merged_df = merged_df.rename(columns={'排名': 'total_rank'})
merged_df = merged_df.rename(columns={'A排名': 'A_rank'})
merged_df = merged_df.rename(columns={'B排名': 'B_rank'})
merged_df = merged_df.rename(columns={'C排名': 'C_rank'})
merged_df = merged_df.rename(columns={'D排名': 'D_rank'})
merged_df = merged_df.rename(columns={'E排名': 'E_rank'})

merged_df = merged_df.rename(columns={'省份': 'province'})
merged_df = merged_df.rename(columns={'时间': 'year'})
# 保存合并后的DataFrame到新的.xlsx文件
merged_df.to_excel('../../public/data/temp/04_百分制转换/合并后的文件.xlsx', index=False)
merged_df.to_excel('../../public/data/result/output/scores_data.xlsx', index=False)
print("文件已合并并保存到 '合并后的文件.xlsx'")