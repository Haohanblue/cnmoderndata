import os
import pandas as pd

# 创建一个新的文件夹用于存放合并后的文件
output_folder = '../../../public/data/temp/03_得分计算/03_3_先直后墒/01_标准化数据'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取normalized_data文件夹下的所有文件
input_folder = '../../../public/data/temp/03_得分计算/02_标准化数据'
input_files = os.listdir(input_folder)

# 遍历每个文件
for file in input_files:
    # 读取 Excel 文件
    df = pd.read_excel(os.path.join(input_folder, file))

    # 获取从第三列开始的列名
    columns_to_merge = df.columns[2:]

    # 新建一个 DataFrame 用于存放合并后的数据
    merged_df = pd.DataFrame()

    # 遍历每个字母
    for letter in sorted(set([col[0] for col in columns_to_merge])):
        # 选择以当前字母开头的列
        cols_with_letter = [col for col in columns_to_merge if col.startswith(letter)]
        # 合并并计算平均值
        merged_df[letter] = df[cols_with_letter].mean(axis=1)

    # 添加原始文件的前两列
    merged_df['省份'] = df['省份']
    merged_df['时间'] = df['时间']

    # 按照ABCDE的顺序排列列
    merged_df = merged_df[['省份', '时间'] + sorted(merged_df.columns[:-2])]

    # 将合并后的数据保存到新的 Excel 文件中
    output_file = os.path.join(output_folder, f'merged_{file}')
    merged_df.to_excel(output_file, index=False)

print("合并完成！")
