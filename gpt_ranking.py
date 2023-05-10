from patent_db import gen_db
import pandas as pd
import openai
import config

# Define a function to compute the text similarity between two strings using GPT-3
def compute_similarity(query, text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Similarity between '{query}' and '{text}':",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return float(response.choices[0].text.strip())


# Initialize the OpenAI API client
openai.api_key = config.openai_api_key

# Define your search query
search_query = "self driving"

# creating patent workspace based on results

path = "C:\\Users\\westw\\Documents\\Project\\patent_search_helper\\gp-search-telsa.csv"

df = gen_db(path)

# Compute the similarity scores between the search query and each row in the dataframe
similarity_scores = df["Claims"].apply(lambda x: compute_similarity(search_query, x))

# Add the similarity scores to the dataframe
df["similarity_score"] = similarity_scores

# Sort the dataframe by similarity score in descending order
df_sorted = df.sort_values(by="similarity_score", ascending=False)

df_sorted.to_csv("sorted results", index=False)