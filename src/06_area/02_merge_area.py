import pandas as pd
import os

# Define a dictionary that maps provinces to regions
region_dict = {
    '北京': '华北地区', '天津': '华北地区', '河北': '华北地区', '山西': '华北地区', '内蒙古': '华北地区',
    '辽宁': '东北地区', '吉林': '东北地区', '黑龙江': '东北地区',
    '上海': '华东地区', '江苏': '华东地区', '浙江': '华东地区', '安徽': '华东地区', '福建': '华东地区', '江西': '华东地区', '山东': '华东地区',
    '河南': '华中地区', '湖北': '华中地区', '湖南': '华中地区',
    '广东': '华南地区', '广西': '华南地区', '海南': '华南地区',
    '重庆': '西南地区', '四川': '西南地区', '贵州': '西南地区', '云南': '西南地区', '西藏': '西南地区',
    '陕西': '西北地区', '甘肃': '西北地区', '青海': '西北地区', '宁夏': '西北地区', '新疆': '西北地区'
}
divisor_dict = {
    '华北地区': 5, '东北地区': 3, '华东地区': 7, '华中地区': 3, '华南地区': 3, '西南地区': 5, '西北地区': 5
}
# Specify the directory where the files are located
input_dir = '../../public/data/temp/05_地区计算/yearly_data'
output_path = '../../public/data/temp/05_地区计算/area_data'
if not os.path.exists(output_path):
    os.makedirs(output_path)
# Get a list of all Excel files in the directory
xlsx_files = [file for file in os.listdir(input_dir) if file.endswith('.xlsx')]

# Iterate over the Excel files
for file_name in xlsx_files:
    # Construct the full file path
    file_path = os.path.join(input_dir, file_name)

    # Read the Excel file
    df = pd.read_excel(file_path)

    # Drop the last six columns
    df = df.iloc[:, :-6]

    # Add a new column 'region', mapping each 'province' to its corresponding region
    df['region'] = df['province'].map(region_dict)

    # Group by 'region' and 'year', and sum the other columns
    grouped = df.groupby(['region', 'year']).sum().reset_index()

    # Drop the 'province' column
    grouped = grouped.drop(columns=['province'])
    # Add a new column 'divisor', mapping each 'region' to its corresponding divisor
    grouped['divisor'] = grouped['region'].map(divisor_dict)

    # Divide each row of data by the corresponding divisor
    for column in grouped.columns:
        if column not in ['region', 'year', 'divisor']:
            grouped[column] = round(grouped[column] / grouped['divisor'])

    # Drop the 'divisor' column
    grouped = grouped.drop(columns=['divisor'])

    # Calculate the rank for each column and add new columns for the ranks
    # Calculate the rank for each column and add new columns for the ranks
    for column in grouped.columns[2:8]:
        grouped[column + '_rank'] = grouped[column].rank(ascending=False, method='min')

    # Write the grouped DataFrame to a new Excel file, using the region and year as the file name
    grouped.to_excel(os.path.join(output_path, f'{grouped["region"].unique()[0]}_{grouped["year"].unique()[0]}.xlsx'),
                     index=False)