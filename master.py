import pandas as pd
import numpy as np
#
# # 100 ta parvoz ma'lumotlari
# np.random.seed(42)
#
# data = {
#     "FlightID": range(1, 101),
#     "Airline": np.random.choice(["UzAirways", "TurkishAir", "Emirates", "Aeroflot"], 100),
#     "DepDelay": np.random.randint(0, 120, 100),  # kechikish (daqiqa)
#     "ScheduledDuration": np.random.randint(60, 300, 100),  # rejalashtirilgan davomiylik (daqiqa)
#     "Origin": np.random.choice(["TAS", "URT", "DXB", "IST", "LHR"], 100),
#     "Destination": np.random.choice(["DXB", "IST", "LHR", "MOW", "NYC"], 100)
# }
#
# df = pd.DataFrame(data)
#
# # CSV faylga yozish
# df.to_csv("flights.csv", index=False)
#
# print(df.head())


from collections import Counter

from numpy.random import random

# df = pd.read_csv("flights.csv")
# print(df.head())
# print(df.describe())
# max = df['DepDelay'].max()
# min = df['DepDelay'].min()
# print(max)
# print(min)
# a = Counter(df['DepDelay'])
# print(a)
d = np.random.randint(1, 14, size=100)
# print(type(d))


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Ali", "Vali", "Gulbahor", "Umid"],
    "Age": [20, 25, 30, 22]
})

# Tasodifiy ballar qo'shish
df["RandomScore"] = np.random.randint(50, 100, size=len(df))
# df = df.reset_index()
# print(df)
# df1 = df.drop(columns=['index'])
# print(df1)
# df.drop(columns=['index'], inplace=True)
# df = df.drop('index', axis=1)
# print(df)
#
# print(df[(df["RandomScore"] > 70) & (df["RandomScore"] < 85)])




