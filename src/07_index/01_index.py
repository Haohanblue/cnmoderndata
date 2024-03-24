import pandas as pd
import os
# Define the data
basic_indicators = ['常住人口出生率', '常住人口死亡率', '常住人口自然增长率', '平均预期寿命', '常住人口抚养比', '每十万人口高等学校平均在校生数', '人均GDP基尼系数', '城镇化率', '城镇登记失业率', '粗离婚率', '城市居民最低生活保障人数', '农村居民最低生活保障人数', '孤儿数', '人均农村居民消费支出', '人均城镇居民消费支出', '人均城市道路面积', '城市每万人拥有公共交通车辆', '城市道路照明灯', '互联网普及率', '城镇居民每百户家用电脑拥有量', '居民平均每百户年末移动电话拥有量', '单位人口拥有公共图书馆藏量', '艺术表演场馆演出场次', '每万人博物馆文物藏品', '博物馆从业人员', '规模以上工业企业R&D经费/GDP', '地方财政教育支出/GDP', '城市绿地面积', '人均公园绿地面积', '自然保护区占辖区面积比重', '环境保护支出', '万元GDP能源消费量', '生活垃圾清运量', '每万人拥有公共厕所', '城市污水日处理能力', '第一产业增加值占比', '第二产业增加值占比', '第三产业增加值占比', '人均GDP', '人均一般公共预算收入', '人均实际利用外资', '人均对外直接投资净额', '人均境内货源地出口总额', '人均境内目的地进口总额']
units = ['%', '%', '%', '岁', '%', '人', '无', '%', '%', '%', '人', '人', '人', '元', '元', '平方米', '标台', '千盏', '%', '台', '台', '册', '万场次', '件', '人', '%', '%', '公顷', '平方米', '%', '亿元', '吨标准煤/万元', '万吨', '座/万人', '万立方米', '%', '%', '%', '元/人', '元/人', '美元/人', '美元/人', '美元/人', '美元/人']
indicator_codes = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9']

# Convert the data to pandas DataFrames
df_basic_indicators = pd.DataFrame(basic_indicators, columns=['基础指标'])
df_units = pd.DataFrame(units, columns=['单位'])
df_indicator_codes = pd.DataFrame(indicator_codes, columns=['指标代码'])

# Concatenate the DataFrames along axis 1
df = pd.concat([df_basic_indicators, df_units, df_indicator_codes], axis=1)
output_file = '../../public/data/result/output/index.xlsx'
if not output_file:
    os.makedirs(output_file)
# Write the DataFrame to an Excel file
df.to_excel(output_file, index=False)