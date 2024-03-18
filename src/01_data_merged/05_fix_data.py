import pandas as pd
import re
import os
# 从 Excel 读取数据
file_path = '../../public/data/temp/01_初次合并/2_转置后的结果.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path)
if not os.path.exists('../../public/data/result'):
    os.makedirs('../../public/data/result')
# 获取列名列表，从第三列开始
columns = df.columns[2:]

# 定义指标名的逻辑顺序
logical_order = [f'{letter}{number}' for letter in 'ABCDE' for number in range(1, 100)]

# 重新排列列名以确保其按照逻辑顺序排列
sorted_columns = sorted(columns, key=lambda x: (re.match(r'([A-Z]+)(\d+)', x).groups()[0], int(re.match(r'([A-Z]+)(\d+)', x).groups()[1])))

# 更新 DataFrame 中的列顺序
df = df[df.columns[:2].tolist() + sorted_columns].copy()
# 将 "--" 替换为空字符串
df.replace("--", "", regex=True, inplace=True)
df.replace("-", "", regex=True, inplace=True)
df.replace(0, "", regex=True, inplace=True)
# 筛选时间列为2000-2023之间的数据
df = df[df['时间'].astype(int).between(2000, 2023)]

# 保存调整后的结果到新的 Excel 文件
adjusted_file_path = '../../public/data/temp/01_初次合并/3_调整后的结果.xlsx'  # 请替换为你的文件路径
df.to_excel(adjusted_file_path, index=False)
adjusted_file_path_2 = '../../public/data/result/原始数据.xlsx'  # 请替换为你的文件路径
df.to_excel(adjusted_file_path_2, index=False)
adjusted_file_path_3 = '../../public/data/result/output/source_data.xlsx'  # 请替换为你的文件路径
df.to_excel(adjusted_file_path_3, index=False)
# 打印结果路径
print(f"调整后的结果保存至：{adjusted_file_path},同时保存至:{adjusted_file_path_2}")
