import pandas as pd
from pyzipcode import ZipCodeDatabase

# Initialize the ZipCodeDatabase
zcdb = ZipCodeDatabase()

# Dictionary to map state abbreviations to full names
state_abbreviation_to_name = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
    "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
    "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire",
    "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
    "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
    "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming", "DC": "District of Columbia"
}

# Function to get state and validate ZIP code using pyzipcode
def get_state_from_zip(zip_code):
    try:
        zip_info = zcdb[zip_code]
        state_abbr = zip_info.state  # Get the state abbreviation
        return state_abbreviation_to_name.get(state_abbr, "-")
    except:
        return "-"


#Main excel file
df = pd.read_excel('resultsM.xlsx')

# function to fill in the state
df['State_1'] = df['Zip'].apply(get_state_from_zip)

output_file_path = 'results_with_zipcode.xlsx'  # Specify the path for the output file
df.to_excel(output_file_path, index=False)