import pandas as pd

# 省份顺序
province_list = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']

# 从 Excel 读取数据
file_path = '../../public/data/temp/01_初次合并/1_合并后的数据.xlsx'  # 请替换为你的文件路径
df = pd.read_excel(file_path)

# 使用 pd.melt 将宽格式转为长格式
melted_df = pd.melt(df, id_vars=['时间', '指标名'], var_name='省份', value_name='值')

# 使用 pivot 创建你想要的结果
result_df = melted_df.pivot(index=['省份', '时间'], columns='指标名', values='值').reset_index()

# 转换省份列为 Categorical，并按指定顺序排序
result_df['省份'] = pd.Categorical(result_df['省份'], categories=province_list, ordered=True)

# 按照省份和时间升序排列
result_df = result_df.sort_values(['省份', '时间'])

# 保存结果到新的 Excel 文件
result_file_path = '../../public/data/temp/01_初次合并/2_转置后的结果.xlsx'  # 请替换为你的文件路径
result_df.to_excel(result_file_path, index=False)

# 打印结果路径
print(f"转置后的结果保存至：{result_file_path}")
