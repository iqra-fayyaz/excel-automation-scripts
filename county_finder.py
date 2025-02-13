import pandas as pd


sheet1 = pd.read_excel(r"C:\Users\PMLS\PycharmProjects\databases\zip_code_database.xlsx")  # File with zipcodes, city, state, and county
sheet2 = pd.read_excel("Book1.xlsx")  # File with address, city, state, and zipcode

sheet1['City'] = sheet1['City']
sheet1['Zip'] = sheet1['Zip']
sheet2['City'] = sheet2['City']
sheet2['Zip'] = sheet2['Zip']


# Drop duplicate cities in sheet1, keeping the first occurrence
sheet1 = sheet1.drop_duplicates(subset=['City', 'Zip'])

# Merge the sheets based on 'City' and 'State'
merged_data = sheet2.merge(sheet1[['City', 'Zip', 'County']], on=['City', 'Zip'], how='left')

# Save the updated sheet with the county column added
merged_data.to_excel("county_results.xlsx", index=False)