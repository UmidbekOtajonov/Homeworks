# # Homework: Pandas Basics
#"""1"""
# import sqlite3
# import pandas as pd
#
# # Connect to the database
# conn = sqlite3.connect("chinook.db")
#
# # Read the customers table into a DataFrame
# customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
#
# # Display first 10 rows
# print(customers_df.head(10))
#
# """2"""
# iris_df = pd.read_json("iris.json")
#
# print("Shape:", iris_df.shape)
# print("Columns:", iris_df.columns.tolist())
#
# """3"""
# titanic_df = pd.read_excel("titanic.xlsx")
#
# print(titanic_df.head(5))
#
# """4"""
# flights_df = pd.read_parquet("flights.parquet")
#
# flights_df.info()
#
# """5"""
# movie_df = pd.read_csv("movie.csv")
#
# print(movie_df.sample(10))

"""Part 2: Exploring DataFrame"""
# #1. Rename columns to lowercase
# iris_df.columns = iris_df.columns.str.lower()
#
# # Select only sepal_length and sepal_width
# iris_selected = iris_df[["sepal_length", "sepal_width"]]
#
# print(iris_selected.head())
#
# #2. Filter rows where age > 30
# titanic_over30 = titanic_df[titanic_df["Age"] > 30]
#
# print(titanic_over30.head())
#
# # Count male and female passengers
# gender_counts = titanic_df["Sex"].value_counts()
#
# print(gender_counts)
#
# # 3 Extract only origin, dest, carrier
# flights_subset = flights_df[["origin", "dest", "carrier"]]
#
# print(flights_subset.head())
#
# # Number of unique destinations
# unique_dest_count = flights_df["dest"].nunique()
#
# print("Unique destinations:", unique_dest_count)
#
# # 4. Filter rows where duration > 120
# long_movies = movie_df[movie_df["duration"] > 120]
#
# # Sort by director_facebook_likes descending
# sorted_long_movies = long_movies.sort_values(
#     by="director_facebook_likes", ascending=False
# )
#
# print(sorted_long_movies.head())
#
#
# """Part 3: Challenges and Explorations  """
# # 1. Calculate mean, median, std for each numerical column
# iris_stats = iris_df.describe().loc[["mean", "50%", "std"]]
#
# print(iris_stats)
# # 2.
# min_age = titanic_df["Age"].min()
# max_age = titanic_df["Age"].max()
# sum_age = titanic_df["Age"].sum()
#
# print("Min age:", min_age)
# print("Max age:", max_age)
# print("Sum of ages:", sum_age)
#
# # 3.
# director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum()
# top_director = director_likes.idxmax()
# top_likes = director_likes.max()
#
# print("Top director:", top_director, "with likes:", top_likes)
#
# longest_movies = movie_df.nlargest(5, "duration")[["movie_title", "director_name", "duration"]]
#
# print(longest_movies)
#
#
# # 4.Flights Parquet file
# missing_values = flights_df.isnull().sum()
# print(missing_values)
#
#
# # Example: fill missing in 'dep_delay' column
# mean_dep_delay = flights_df["dep_delay"].mean()
# flights_df["dep_delay"].fillna(mean_dep_delay, inplace=True)
#

















