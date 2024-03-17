import os
import pandas as pd

# 读取Excel文件
file_path = '../../../public/data/temp/03_得分计算/03_2_先墒后直/分项合并数据.xlsx'
df = pd.read_excel(file_path)

# 按时间分组
grouped = df.groupby('时间')

# 创建新文件夹保存分组数据
output_folder = '../../../public/data/temp/03_得分计算/03_4_先墒后墒/01_时间数据'
os.makedirs(output_folder, exist_ok=True)

# 遍历每个分组，保存到对应的文件中
for time, group_data in grouped:
    # 创建以时间命名的文件夹

    # 保存分组数据到新的Excel文件中
    output_file_path = os.path.join(output_folder, f'{time}.xlsx')
    group_data.to_excel(output_file_path, index=False)
    print(f'文件保存至：{output_file_path}')
