import os
import pandas as pd

# 设置输入文件夹路径和输出文件夹路径
input_folder = '../../../public/data/temp/03_得分计算/02_标准化数据'
output_folder = '../../../public/data/temp/03_得分计算/03_2_先墒后直/01_标准化数据'
os.makedirs(output_folder, exist_ok=True)

# 获取输入文件夹中所有.xlsx文件
file_names = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

# 遍历每个文件执行相同的操作
for file_name in file_names:
    file_path = os.path.join(input_folder, file_name)
    df = pd.read_excel(file_path)

    # 获取省份和时间列
    province_time = df[['省份', '时间']]

    # 获取除省份和时间列外的数据列
    data_columns = df.columns[2:]

    # 根据列名规则，拆分数据到不同的 DataFrame 中
    grouped_data = {}
    for col in data_columns:
        prefix = col[0]  # 获取列名的首字母作为前缀
        if prefix not in grouped_data:
            grouped_data[prefix] = pd.concat([province_time, df[col]], axis=1)
        else:
            grouped_data[prefix] = pd.concat([grouped_data[prefix], df[col]], axis=1)

    # 提取年份作为文件名的一部分
    year = file_name[-9:-5]

    # 将每个前缀对应的数据保存到对应的文件夹中
    for prefix, data_df in grouped_data.items():
        folder_path = os.path.join(output_folder, prefix)
        os.makedirs(folder_path, exist_ok=True)
        new_file_name = f'{year}_{prefix}_data.xlsx'
        file_path = os.path.join(folder_path, new_file_name)
        data_df.to_excel(file_path, index=False)
        print(f'数据保存至：{file_path}')

print("数据拆分并保存完成。")
