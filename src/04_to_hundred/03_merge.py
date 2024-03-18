import os
import pandas as pd

# 输入文件夹路径和输出文件路径
input_folder = '../../public/data/temp/04_百分制转换/分项数据'
input_folder_2 = '../../public/data/temp/04_百分制转换/总得分'
output_file = '../../public/data/temp/04_百分制转换/分项数据.xlsx'
output_file_2 = '../../public/data/temp/04_百分制转换/总得分.xlsx'
# 初始化一个空的DataFrame用于存储所有文件的数据
combined_df = pd.DataFrame()

# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder):
    # 检查文件是否是.xlsx文件
    if file_name.endswith('.xlsx'):
        # 获取文件的完整路径
        input_file_path = os.path.join(input_folder, file_name)

        # 读取XLSX文件
        df = pd.read_excel(input_file_path)

        # 将读取的数据添加到combined_df中
        combined_df = pd.concat([combined_df, df])

# 保存合并后的DataFrame到新的.xlsx文件
combined_df.to_excel(output_file, index=False)

combined_df = pd.DataFrame()
# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder_2):
    # 检查文件是否是.xlsx文件
    if file_name.endswith('.xlsx'):
        # 获取文件的完整路径
        input_file_path_2 = os.path.join(input_folder_2, file_name)

        # 读取XLSX文件
        df = pd.read_excel(input_file_path_2)

        # 从文件名中获取年份信息
        year = int(file_name[-9:-5])  # 假设年份信息在文件名的末尾，例如"file_2022.xlsx"

        # 在DataFrame中添加一个新的列来存储年份信息
        df['时间'] = year

        # 将读取的数据添加到combined_df中
        combined_df = pd.concat([combined_df, df])

# 保存合并后的DataFrame到新的.xlsx文件
combined_df.to_excel(output_file_2, index=False)

# 保存合并后的DataFrame到新的.xlsx文件
combined_df.to_excel(output_file_2, index=False)
print(f"所有文件已合并并保存到 {output_file_2}")