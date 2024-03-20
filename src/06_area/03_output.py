import pandas as pd
import os

# Specify the directory where the files are located
input_dir = '../../public/data/temp/05_地区计算/area_data'

# Get a list of all Excel files in the directory
xlsx_files = [file for file in os.listdir(input_dir) if file.endswith('.xlsx')]

# Initialize an empty list to store the dataframes
dfs = []

# Iterate over the Excel files
for file_name in xlsx_files:
    # Construct the full file path
    file_path = os.path.join(input_dir, file_name)

    # Read the Excel file and append the dataframe to the list
    dfs.append(pd.read_excel(file_path))

# Concatenate all dataframes in the list
merged_df = pd.concat(dfs, ignore_index=True)
# Specify the output file path
output_file = '../../public/data/temp/05_地区计算/area_data.xlsx'
if not output_file:
    os.makedirs(output_file)
output_file_2 = '../../public/data/result/output/area_data.xlsx'
if not output_file_2:
    os.makedirs(output_file_2)
# Write the merged DataFrame to the output file
merged_df.to_excel(output_file, index=False)
merged_df.to_excel(output_file_2, index=False)