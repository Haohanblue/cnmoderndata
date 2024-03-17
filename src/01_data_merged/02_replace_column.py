import os
import pandas as pd

# 获取当前文件夹路径
current_folder = "../../public/data/source"

# 获取当前文件夹下所有xlsx文件的文件名列表
xlsx_files = [file for file in os.listdir(current_folder) if file.endswith('.xlsx')]

# 提供的省级行政区划列表
province_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']

# 遍历每个xlsx文件进行匹配操作
for file_name in xlsx_files:
    # 构建完整的文件路径
    file_path = os.path.join(current_folder, file_name)

    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path)

    # 获取列名并转换为列表
    column_names = df.columns.tolist()

    # 从第二列开始替换列名
    for i in range(1, len(column_names)):
        df.rename(columns={column_names[i]: province_list[i-1]}, inplace=True)

    # 保存修改后的文件
    df.to_excel(file_path, index=False)
    print(f"文件 '{file_name}' 的列名从第二列开始已替换并保存。")
