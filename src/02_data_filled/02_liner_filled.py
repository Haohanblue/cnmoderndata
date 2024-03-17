import os
import pandas as pd

# 创建新文件夹来存放处理后的文件
output_folder_interpolated = '../../public/data/temp/02_数据处理与填充/02_省份数据_插值填充'
os.makedirs(output_folder_interpolated, exist_ok=True)

# 遍历指定文件夹中的每个 xlsx 文件
input_folder = '../../public/data/temp/02_数据处理与填充/01_省份数据'
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(input_folder, file_name)

        # 读取 Excel 文件
        df = pd.read_excel(file_path)

        # 遍历每一列
        for column in df.columns:
            # 遍历每一行
            i = 1  # 从第二行开始
            while i < len(df) - 1:
                # 如果当前位置的数据为空值
                this = df.at[i, column]
                if pd.isnull(this):
                    # 向上寻找非空值
                    up_index = i - 1
                    while up_index >= 0 and pd.isnull(df.at[up_index, column]):
                        up_index -= 1
                    # 向下寻找非空值
                    down_index = i + 1
                    while down_index < len(df) and pd.isnull(df.at[down_index, column]):
                        down_index += 1
                    # 如果上下都找到了非空值，则使用插值法填充当前位置
                    if up_index >= 0 and down_index < len(df):
                        up = df.at[up_index, column]
                        down = df.at[down_index, column]
                        if not pd.isnull(up) and not pd.isnull(down):
                            dist = (down - up) / (down_index - up_index)
                            df.at[i, column] = up + dist * (i - up_index)

                i += 1  # 继续下一行

        # 生成新文件名和路径
        new_file_name = file_name.replace('.xlsx', '_插值填充.xlsx')
        new_file_path = os.path.join(output_folder_interpolated, new_file_name)

        # 保存处理后的数据到新文件夹
        df.to_excel(new_file_path, index=False)
        print(f"处理后的数据已保存至 {new_file_path}")
