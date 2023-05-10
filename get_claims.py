import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_claims_from_gp(patent_links):
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
