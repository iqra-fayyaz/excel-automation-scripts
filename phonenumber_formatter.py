import re
import pandas as pd


def convert_phone_number(ph):
    # Use regex to extract the digits from the input phone number
    match = re.match(r'\+1 (\d{3})-(\d{3})-(\d{4})', phone)
    if match:
        # Format the extracted digits into the desired format
        return f"({match.group(1)}) {match.group(2)} {match.group(3)}"
    else:
        return "Invalid format"

# Example usage:
df = pd.read_excel("Book1.xlsx")
df['phone'] = df['Phone'].apply(convert_phone_number)
df.to_excel("number(modified).xlsx")
