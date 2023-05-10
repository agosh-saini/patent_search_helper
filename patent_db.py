import pandas as pd
from get_claims import fetch_claims_from_gp

def gen_db(path):
    # "C:\\Users\\westw\\Documents\\Project\\patent_search_helper\\gp-search-telsa.csv"

    # working db
    df_raw = pd.read_csv(path, skiprows=1)

    # get patent links as key
    patent_links = df_raw['result link'].to_numpy()

    # Fetch the claims data
    claims_data = fetch_claims_from_gp(patent_links)

    # Create a pandas DataFrame
    claims_df = pd.DataFrame(claims_data, columns=['Patent Link', 'Patent Number', 'Claims'])

    # create db
    claims_df.to_csv("patent_db.csv", index=False)

    return claims_df
