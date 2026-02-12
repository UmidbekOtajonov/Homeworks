# Task 1: Weather API
# import requests
#
# # Replace with your actual API key from OpenWeatherMap
# API_KEY = "your_api_key_here"
# CITY = "Tashkent"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#
# # Build request URL
# url = f"{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric"
#
# # Send GET request
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#
#     # Extract relevant information
#     city = data["name"]
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     weather_desc = data["weather"][0]["description"]
#
#     print(f"Weather in {city}:")
#     print(f"Temperature: {temperature}°C")
#     print(f"Humidity: {humidity}%")
#     print(f"Condition: {weather_desc}")
# else:
#     print("Error fetching data:", response.status_code)
#
#
# # Task 2: Movie Recommendation System
#
# import requests
# import random
#
# API_KEY = "your_api_key_here"  # TMDb API kalitingizni yozing
# BASE_URL = "https://api.themoviedb.org/3"
#
#
# def get_genre_id(genre_name):
#     """Berilgan janr nomidan genre_id topadi"""
#     url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
#     response = requests.get(url)
#     if response.status_code == 200:
#         genres = response.json()["genres"]
#         for genre in genres:
#             if genre["name"].lower() == genre_name.lower():
#                 return genre["id"]
#     return None
#
#
# def recommend_movie(genre_name):
#     """Berilgan janr bo‘yicha random film tavsiya qiladi"""
#     genre_id = get_genre_id(genre_name)
#     if genre_id is None:
#         print("Bunday janr topilmadi.")
#         return
#
#     url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
#     response = requests.get(url)
#     if response.status_code == 200:
#         movies = response.json()["results"]
#         if movies:
#             movie = random.choice(movies)
#             print(f" Tavsiya: {movie['title']}")
#             print(f" Yili: {movie['release_date']}")
#             print(f" Reyting: {movie['vote_average']}")
#             print(f" Tavsif: {movie['overview']}")
#         else:
#             print("Bu janrda film topilmadi.")
#     else:
#         print("Xatolik yuz berdi:", response.status_code)
#
#
# # Foydalanuvchidan janr so‘rash
# genre_input = input("Qaysi janrni xohlaysiz? (Masalan: Action, Comedy, Drama): ")
# recommend_movie(genre_input)

