import os
import pandas as pd

# 创建一个空的 DataFrame 用于存储合并后的数据
merged_df = pd.DataFrame()

# 遍历省份数据_插值填充文件夹中的每个文件
input_folder = '../../public/data/temp/02_数据处理与填充/03_省份数据_预测填充'
for file_name in os.listdir(input_folder):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(input_folder, file_name)

        # 读取 Excel 文件，跳过首行
        df = pd.read_excel(file_path)

        # 将当前文件的数据追加到 merged_df 中
        merged_df = pd.concat([merged_df, df], ignore_index=True)

# 按照指定的省份顺序和时间列的升序对数据进行排序
province_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
merged_df['省份'] = pd.Categorical(merged_df['省份'], categories=province_list, ordered=True)
merged_df = merged_df.sort_values(['省份', '时间'])

# 保存合并后的数据到新的 Excel 文件
output_file_path = '../../public/data/temp/02_数据处理与填充/04_合并后的填充数据.xlsx'
merged_df.to_excel(output_file_path, index=False)

output_file_path_2 = '../../public/data/result/完整数据.xlsx'
merged_df.to_excel(output_file_path_2, index=False)
merged_df = merged_df.rename(columns={'省份': 'province'})
merged_df = merged_df.rename(columns={'时间': 'year'})
output_file_path_3 = '../../public/data/result/output/filled_data.xlsx'
merged_df.to_excel(output_file_path_3, index=False)
print(f'数据已成功合并并按照指定的省份顺序和时间升序保存到 {output_file_path}，同时保存到了{output_file_path_2}')
