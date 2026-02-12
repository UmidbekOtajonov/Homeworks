#### **Merging and Joining**
# #Task1.
# import sqlite3
# import pandas as pd
#
# # 1. Connect to the Chinook database
# conn = sqlite3.connect("chinook.db")
#
# # 2. Load customers and invoices tables into Pandas DataFrames
# customers = pd.read_sql_query("SELECT * FROM customers", conn)
# invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
#
# # 3. Perform INNER JOIN on CustomerId
# merged_df = pd.merge(customers, invoices, on="CustomerId", how="inner")
#
# # 4. Group by CustomerId and count invoices
# invoice_counts = (
#     merged_df.groupby(["CustomerId", "FirstName", "LastName"])
#     .agg(TotalInvoices=("InvoiceId", "count"))
#     .reset_index()
#     .sort_values(by="TotalInvoices", ascending=False)
# )
#
# # 5. Display result
# print(invoice_counts.head(10))  # show top 10 customers
#
# #Task2.
# import pandas as pd
#
# # 1. Load the movie.csv file
# movies = pd.read_csv("movie.csv")
#
# # 2. Create two smaller DataFrames
# df1 = movies[["director_name", "color"]]
# df2 = movies[["director_name", "num_critic_for_reviews"]]
#
# # 3. Perform LEFT JOIN on director_name
# left_join = pd.merge(df1, df2, on="director_name", how="left")
#
# # 4. Perform FULL OUTER JOIN on director_name
# outer_join = pd.merge(df1, df2, on="director_name", how="outer")
#
# # 5. Count rows in each resulting DataFrame
# print("Rows in LEFT JOIN:", len(left_join))
# print("Rows in FULL OUTER JOIN:", len(outer_join))



#### **Grouping and Aggregating**
# #Task1.
# import pandas as pd
#
# # 1. Load Titanic dataset
# titanic = pd.read_csv("titanic.csv")
#
# # 2. Group passengers by Pclass and calculate aggregations
# grouped = (
#     titanic.groupby("Pclass")
#     .agg(
#         AverageAge=("Age", "mean"),
#         TotalFare=("Fare", "sum"),
#         PassengerCount=("PassengerId", "count")
#     )
#     .reset_index()
# )
#
# # 3. Save results to a new DataFrame
# results_df = grouped
#
# # 4. Display results
# print(results_df)
#
#
# #Task2.
# import pandas as pd
#
# # 1. Load movie dataset
# movies = pd.read_csv("movie.csv")
#
# # 2. Multi-level grouping by color and director_name
# grouped = (
#     movies.groupby(["color", "director_name"])
#     .agg(
#         TotalCriticReviews=("num_critic_for_reviews", "sum"),
#         AverageDuration=("duration", "mean")
#     )
#     .reset_index()
# )
#
# # 3. Display results
# print(grouped.head(10))  # faqat dastlabki 10 natijani ko‘rsatamiz
#
#
# #Task3.
# import pandas as pd
#
# # 1. Load flights dataset
# flights = pd.read_csv("flights.csv")
#
# # 2. Nested grouping by Year and Month
# grouped = (
#     flights.groupby(["Year", "Month"])
#     .agg(
#         TotalFlights=("FlightNum", "count"),
#         AvgArrDelay=("ArrDelay", "mean"),
#         MaxDepDelay=("DepDelay", "max")
#     )
#     .reset_index()
# )
#
# # 3. Display results
# print(grouped.head(12))  # birinchi 12 oy natijasi
#
#
#### **Applying Functions**
# #Task1.
# import pandas as pd
#
# # 1. Titanic datasetni yuklash
# titanic = pd.read_csv("titanic.csv")
#
# # 2. Custom function yozish
# def classify_age(age):
#     if pd.isnull(age):   # agar Age qiymati NaN bo‘lsa
#         return "Unknown"
#     elif age < 18:
#         return "Child"
#     else:
#         return "Adult"
#
# # 3. apply() yordamida yangi ustun yaratish
# titanic["Age_Group"] = titanic["Age"].apply(classify_age)
#
# # 4. Natijani ko‘rish
# print(titanic[["Age", "Age_Group"]].head(10))
#
# #Task2.
# import pandas as pd
#
# # 1. Load employee dataset
# employees = pd.read_csv("employee.csv")
#
# # 2. Normalize salaries within each department (min-max normalization)
# employees["NormalizedSalary"] = employees.groupby("Department")["Salary"].transform(
#     lambda x: (x - x.min()) / (x.max() - x.min())
# )
#
# # 3. Display results
# print(employees.head(10))
#
# #Task3.
# import pandas as pd
# def classify_movie_duration(duration):
#     """
#     Classify a movie based on its duration.
#
#     Parameters:
#         duration (int or float): Duration of the movie in minutes.
#
#     Returns:
#         str: 'Short', 'Medium', or 'Long'
#     """
#     if duration < 60:
#         return "Short"
#     elif 60 <= duration <= 120:
#         return "Medium"
#     else:
#         return "Long"
#
# # Load dataset
# movies = pd.read_csv("movie.csv")
#
# # Apply classification function
# movies["Category"] = movies["Duration"].apply(classify_movie_duration)
#
# # Preview results
# print(movies.head())
#
#
#### **Using `pipe`**
# #Task1.
# import pandas as pd
#
# # Titanic datasetni o'qish (misol uchun)
# df = pd.read_csv("titanic.csv")
#
# def pipeline_titanic(df):
#     # 1. Faqat tirik qolganlarni filter qilish
#     df = df[df['Survived'] == 1].copy()
#
#     # 2. Age ustunidagi NaN qiymatlarni o'rtacha bilan to'ldirish
#     mean_age = df['Age'].mean()
#     df['Age'] = df['Age'].fillna(mean_age)
#
#     # 3. Yangi ustun yaratish: Fare_Per_Age
#     df['Fare_Per_Age'] = df['Fare'] / df['Age']
#
#     return df
#
# # Misol ishlatish:
# # transformed_df = pipeline_titanic(df)
# # print(transformed_df.head())
#
# #Task2.
# import pandas as pd
#
#
# # Misol uchun flights dataset
# df = pd.read_csv("flights.csv")
#
# def pipeline_flights(df):
#     # 1. Departure delay > 30 bo'lganlarni filter qilish
#     df = df[df['DepDelay'] > 30].copy()
#
#     # 2. Yangi ustun: Delay_Per_Hour
#     # DepDelay (daqiqa) ni ScheduledDuration (daqiqa) ga bo'lamiz
#     df['Delay_Per_Hour'] = df['DepDelay'] / df['ScheduledDuration']
#
#     return df
#
# # Misol ishlatish:
# transformed_df = pipeline_flights(df)
# print(transformed_df.head())








