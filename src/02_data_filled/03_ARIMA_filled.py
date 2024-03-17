import os
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

# 禁用警告信息显示
warnings.filterwarnings("ignore")

# 输入文件夹和输出文件夹路径
input_folder = '../../public/data/temp/02_数据处理与填充/02_省份数据_插值填充'
output_folder = '../../public/data/temp/02_数据处理与填充/03_省份数据_预测填充'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 确定 ARIMA 模型的阶数
order = (1, 0, 1)  # ARIMA(1,0,1)

# 遍历处理后的数据文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.xlsx'):

        # 读取数据
        filepath = os.path.join(input_folder, filename)
        print("正在读取{}".format(filepath))
        df = pd.read_excel(filepath)

        # 获取数据列（从第三列开始）
        data_columns = df.columns[2:]

        # 遍历每个数据列，执行填充操作
        for column in data_columns:
            # 索引非空值
            non_nan_indexes = df[column].notna()
            non_nan_values = df.loc[non_nan_indexes, column]

            # 建立 ARIMA 模型
            model = ARIMA(non_nan_values, order=order)
            model_fit = model.fit()

            # 使用模型填补缺失值
            filled_values = df[column].copy()
            for i in range(len(df[column])):
                if pd.isna(df[column][i]):
                    # 使用 ARIMA 模型进行预测并填充
                    filled_values[i] = model_fit.predict(start=len(non_nan_values) + i, end=len(non_nan_values) + i)

            # 将填充后的数据添加到 DataFrame 中
            df[column] = filled_values

        # 保存填充后的数据到新的 Excel 文件
        new_file_name = filename.replace('_插值填充.xlsx', '_预测填充.xlsx')
        output_filepath = os.path.join(output_folder, new_file_name)
        df.to_excel(output_filepath, index=False)
        print("已经保存{}".format(output_filepath))
print("所有文件的填充后数据已保存到", output_folder, "文件夹中。")
