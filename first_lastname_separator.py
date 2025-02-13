import pandas as pd


df = pd.read_excel('last_merged_file.xlsx')

# Function to separate first and last names
def split_name(full_name):
    if pd.isna(full_name):
        return pd.Series(['', ''])
    cleaned_name = full_name
    if ',' in cleaned_name:
        name_parts = cleaned_name.rsplit(',', 1)  # Split by last comma
        first_name = name_parts[0].strip()  # Take everything before the last comma
        last_name = name_parts[1].strip()

    elif ' and ' in cleaned_name:
        # Split by "and" for multiple names
        parts = cleaned_name.split(' and ')
        first_name = ' '.join(parts[:-1])  # Combine everything before the last "and"
        # Safeguard for when parts[-1] might be empty or unexpected
        last_name_part = parts[-1].split()
        last_name = last_name_part[-1].strip() if last_name_part else ''

    elif ' And ' in cleaned_name:
        # Split by "and" for multiple names
        parts = cleaned_name.split(' And ')
        first_name = ' '.join(parts[:-1])  # Combine everything before the last "and"
        # Safeguard for when parts[-1] might be empty or unexpected
        last_name_part = parts[-1].split()
        last_name = last_name_part[-1].strip() if last_name_part else ''

    elif '&' in cleaned_name:
        # Split by "and" for multiple names
        parts = cleaned_name.split(' and ')
        first_name = ' '.join(parts[:-1])  # Combine everything before the last "and"
        last_name = parts[-1].split()[-1]  # The last word after the last "and" is the last name

    elif '/' in cleaned_name:
        parts = cleaned_name.split('/')
        first_name = parts[0].strip()  # Take the first name part
        last_name_part = parts[-1].split()
        last_name = last_name_part[-1].strip() if last_name_part else ''

    elif '"' in cleaned_name:
        parts = cleaned_name.split('"')
        first_name = parts[0].strip()  # Take the first name part
        last_name_part = parts[-1].split()
        last_name = last_name_part[-1].strip() if last_name_part else ''

    else:
        parts = cleaned_name.split(' ')
        if len(parts) == 1:
            first_name = ''
            last_name = parts[0].strip()
        else:
            first_name = ' '.join(parts[:-1]).strip()  # Everything except the last part
            last_name = parts[-1].strip()  # Last word is the last namee

    return pd.Series([first_name, last_name])


# Apply the function to the DataFrame
df['Name'] = df['Name'].astype(str)
df[['FirstName', 'LastName']] = df['Name'].apply(split_name)


output_file_path = 'output_file_54.9k.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Excel file '{output_file_path}' created successfully.")