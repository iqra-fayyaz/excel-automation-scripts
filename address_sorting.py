#This file separates zip codes, State, City and Street address from provided unformatted address.
import pandas as pd
import re

df = pd.read_excel("Book1.xlsx")


def extract_state(address):
    match = re.search(r'\b([A-Z]{2})\s\d{5}\b', address)
    if match:
        return match.group(1)
    return None

# Separates zip from address
def extract_zip(address):
    match = re.search(r'\d{5}', address)
    if match:
        return match.group(0)
    return None

#Separates City from address
def extract_city(address):
    if address.count(",") == 2:
        return address.split(",")[1].strip()
    elif address.count(",") == 3:
        return address.split(",")[2].strip()
    else:
        return address.split(",")[0].strip()

#Separates Street Address from address
def extract_address(address):
    if address.count(",") == 2:
        return address.split(",")[0].strip()
    elif address.count(",") == 3:
        first_two_values = [part.strip() for part in address.split(",")[:2]]
        return (', '.join(first_two_values))



df['State'] = df['Address'].apply(extract_state)
df['Zip'] = df['Address'].apply(extract_zip)
df['City'] = df['Address'].apply(extract_city)
df['St Address'] = df['Address'].apply(extract_address)
df.to_excel("resultsM.xlsx")