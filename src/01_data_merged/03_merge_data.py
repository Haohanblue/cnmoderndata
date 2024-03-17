import os
import re
import pandas as pd

# 指定包含xlsx文件的文件夹路径
folder_path = '../../public/data/source'
if not os.path.exists('../../public/data/temp/01_初次合并'):
    os.makedirs('../../public/data/temp/01_初次合并')
# 自定义排序函数，按字母和数字的组合顺序进行排序
def custom_sort(file_name):
    match = re.match(r'([A-Z]+)(\d+)\.xlsx', file_name)
    if match:
        letter_part = match.group(1)
        number_part = int(match.group(2))
        return (letter_part, number_part)
    return ('', -1)  # 如果文件名不符合格式，返回空字符串和-1

# 获取文件夹下所有xlsx文件并按字母和数字的组合顺序排序
xlsx_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.xlsx')], key=custom_sort)

# 创建一个空的DataFrame，用于存储合并后的数据
merged_data = pd.DataFrame()

# 逐个读取xlsx文件并追加到merged_data中
for file in xlsx_files:
    # 读取xlsx文件
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)

    # 添加列：指标名
    df.insert(0, '指标名', file[:-5])  # 获取文件名作为指标名，去掉文件扩展名

    # 修改第一列的列名为“时间”
    df = df.rename(columns={df.columns[1]: '时间'})

    # 将当前文件的数据追加到merged_data中
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# 将合并后的数据保存到新的xlsx文件中
output_file_path = '../../public/data/temp/01_初次合并/1_合并后的数据.xlsx'
merged_data.to_excel(output_file_path, index=False)

print(f'数据已成功合并并保存到 {output_file_path}')
