import pandas as pd

file_path = 'data/horror_movies.csv'

df = pd.read_csv(file_path)

# print("--- Here are the first 5 movies in the list ---")
# print(df.head())

# print("\n--- Basic Dataset Info ---")
# print(df.info())

popular_movies = df[df['vote_count'] > 50]
top_rated = popular_movies.sort_values(by='vote_average', ascending=False)

print("\n--- The Top 10 Highest Rated Horror Movies (with > 50 votes) ---")
print(top_rated[['title', 'vote_average']].head(10))

profitable_movies = df[df['revenue'] > 0]
top_revenue = profitable_movies.sort_values(by='revenue', ascending=False)

print("\n--- The Highest Grossing Horror Movies ---")
print(top_revenue[['title', 'revenue']].head(10))

top_revenue.head(10).to_csv('top_10_horror_revenue.csv', index=False)