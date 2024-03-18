import os
import pandas as pd
from sqlalchemy import create_engine

# 连接数据库，输入数据库地址，用户名以及密码，创建新的数据库
engine = create_engine('mysql+pymysql://cnmodern:Haohanblue233@haohan.site:3306/cnmodern')
print("数据库连接成功")

base_url = '../../public/data/result/output'

# 遍历文件夹中的所有文件
for file_name in os.listdir(base_url):
    # 检查文件是否是.xlsx文件
    if file_name.endswith('.xlsx'):
        # 获取文件的完整路径
        file_path = os.path.join(base_url, file_name)

        print(f"开始处理文件：{file_name}")

        # 读取XLSX文件
        df = pd.read_excel(file_path)

        print(f"成功读取文件：{file_name}")

        # 将数据最多显示小数点后6位
        df = df.round(6)

        # 将DataFrame上传至数据库，并创建对应的表
        # 表名为文件名（不包括扩展名）
        table_name = os.path.splitext(file_name)[0]
        df.to_sql(table_name, engine, if_exists='replace', index=False)

        print(f"成功上传数据到表：{table_name}")