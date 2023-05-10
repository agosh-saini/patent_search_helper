from patent_db import gen_db
import pandas as pd

# creating patent workspace based on results

path = "C:\\Users\\westw\\Documents\\Project\\patent_search_helper\\gp-search-telsa.csv"

df = gen_db(path)

print(df)