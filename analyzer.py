import pandas as pd

def get_top_horror_movies(data_path, metric='revenue', top_n=10):
    """
    Loads horror movie data and returns the top movies based on a specific metric.
    """
    # 1. Load data
    df = pd.read_csv(data_path)
    
    # 2. Clean data: Filter out rows where the metric is 0 and votes are low

    filtered_df = df[(df[metric] > 0) & (df['vote_count'] > 50)]
    
    # 3. Sort and grab the top results
    result = filtered_df.sort_values(by=metric, ascending=False).head(top_n)
    
    return result[['title', metric, 'vote_average']]

# --- Main Execution ---
PATH = 'data/horror_movies.csv'

print("--- Top 5 Money Makers ---")
print(get_top_horror_movies(PATH, metric='revenue', top_n=5))

print("\n--- Top 5 Critically Acclaimed ---")
print(get_top_horror_movies(PATH, metric='vote_average', top_n=5))