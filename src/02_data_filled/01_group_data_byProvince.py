import os
import pandas as pd

# 读取调整后的结果.xlsx 文件
file_path = '../../public/data/temp/01_初次合并/3_调整后的结果.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path)

# 按省份列分组
grouped = df.groupby('省份')

# 创建保存拆分数据的文件夹
output_folder = '../../public/data/temp/02_数据处理与填充/01_省份数据'
os.makedirs(output_folder, exist_ok=True)

# 遍历每个省份的数据并保存到对应的文件夹中
for province, data in grouped:
    # 构建当前省份对应的文件名
    province_file = os.path.join(output_folder, f'{province}.xlsx')

    # 保存当前省份的数据到对应的文件中
    data.to_excel(province_file, index=False)
    print(f'保存 {province} 数据到 {province_file}')

print('拆分并保存数据完成')
