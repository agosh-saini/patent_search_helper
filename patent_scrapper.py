import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_google_patent_claims(patent_links):
    claims_data = []

    for link in patent_links:
        try:
            response = requests.get(link)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                patent_number = soup.find('span', itemprop='publicationNumber').text.strip()
                claims = soup.find('section', itemprop='claims')
                claims_data.append((link, patent_number, claims.text.strip()))
            else:
                print(f"Error fetching patent from {link}: {response.status_code}")

        except Exception as e:
            print(f"Error fetching patent from {link}: {e}")

    return claims_data

# Sample list of Google Patents link
path = "C:\\Users\\westw\\Documents\\Project\\patent_search_helper\\gp-search-telsa.csv"

df_raw = pd.read_csv(path, skiprows=1)

patent_links = df_raw['result link'].to_numpy()

# Fetch the claims data
claims_data = fetch_google_patent_claims(patent_links)

# Create a pandas DataFrame
claims_df = pd.DataFrame(claims_data, columns=['Patent Link', 'Patent Number', 'Claims'])

print(claims_df)

claims_df.to_csv("patent_db.csv", index=False)
