import pandas as pd
import os

# Read the Excel file
df = pd.read_excel('../../public/data/temp/04_百分制转换/合并后的文件.xlsx')

# Group the DataFrame by the 'year' column
grouped = df.groupby('year')

# Specify the directory where the files will be saved
output_dir = '../../public/data/temp/05_地区计算/yearly_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Make sure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over the groups
for year, group in grouped:
    # Write the group DataFrame to an Excel file, using the year as the file name
    group.to_excel(os.path.join(output_dir, f'{year}.xlsx'), index=False)