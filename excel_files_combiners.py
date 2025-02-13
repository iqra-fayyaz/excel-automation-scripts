import pandas as pd

# List of Excel file paths
file_list = ['Your\Excel\File\Path\1.xlsx','Your\Excel\File\Path\2.xlsx','Your\Excel\File\Path\3.xlsx']
master_df = pd.DataFrame()

for file in file_list:

    df = pd.read_excel(file)
    master_df = pd.concat([master_df, df], ignore_index=True)

# Save the combined master DataFrame to a new Excel file
master_file_path = 'master_file.csv'  # Replace with your desired output path
master_df.to_excel(master_file_path, index=False)

print(f"Master file created and saved as '{master_file_path}'")