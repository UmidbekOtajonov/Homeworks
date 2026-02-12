# """Task1"""
# from bs4 import BeautifulSoup
#
# # Load the HTML file
# with open("weather.html", "r", encoding="utf-8") as file:
#     html_content = file.read()
#
# # Parse with BeautifulSoup
# soup = BeautifulSoup(html_content, "html.parser")
#
# # Extract table rows
# rows = soup.find("tbody").find_all("tr")
#
# # Store forecast data
# forecast = []
#
# print("5-Day Weather Forecast:")
# for row in rows:
#     cols = row.find_all("td")
#     day = cols[0].text.strip()
#     temp = cols[1].text.strip()
#     condition = cols[2].text.strip()
#
#     forecast.append({"day": day, "temperature": temp, "condition": condition})
#     print(f"{day}: {temp}, {condition}")
#
# # Convert temperature to integer (remove °C)
# for entry in forecast:
#     entry["temp_value"] = int(entry["temperature"].replace("°C", ""))
#
# # Find highest temperature
# max_temp = max(entry["temp_value"] for entry in forecast)
# hottest_days = [entry["day"] for entry in forecast if entry["temp_value"] == max_temp]
#
# # Find Sunny days
# sunny_days = [entry["day"] for entry in forecast if entry["condition"].lower() == "sunny"]
#
# print(f"\nHighest Temperature: {max_temp}°C on {', '.join(hottest_days)}")
# print(f"Sunny Days: {', '.join(sunny_days)}")
#
# avg_temp = sum(entry["temp_value"] for entry in forecast) / len(forecast)
# print(f"\nAverage Temperature: {avg_temp:.2f}°C")
#
#
# """Task2"""
#
# import requests
# from bs4 import BeautifulSoup
# import sqlite3
# import csv
#
# # -----------------------------
# # Step 1: Scrape Job Listings
# # -----------------------------
# def scrape_jobs(url="https://realpython.github.io/fake-jobs/"):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     jobs = []
#     job_cards = soup.find_all("div", class_="card-content")
#
#     for card in job_cards:
#         title = card.find("h2", class_="title").text.strip()
#         company = card.find("h3", class_="subtitle").text.strip()
#         location = card.find("p", class_="location").text.strip()
#         description = card.find("div", class_="content").text.strip()
#         link = card.find("a")["href"]
#
#         jobs.append({
#             "title": title,
#             "company": company,
#             "location": location,
#             "description": description,
#             "link": link
#         })
#     return jobs
#
#
# # -----------------------------
# # Step 2: Setup SQLite Database
# # -----------------------------
# def setup_database(db_name="jobs.db"):
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS jobs (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             company TEXT,
#             location TEXT,
#             description TEXT,
#             link TEXT,
#             UNIQUE(title, company, location)
#         )
#     """)
#     conn.commit()
#     return conn
#
#
# # -----------------------------
# # Step 3: Incremental Load + Update Tracking
# # -----------------------------
# def save_jobs(conn, jobs):
#     cursor = conn.cursor()
#     for job in jobs:
#         try:
#             cursor.execute("""
#                 INSERT INTO jobs (title, company, location, description, link)
#                 VALUES (?, ?, ?, ?, ?)
#             """, (job["title"], job["company"], job["location"], job["description"], job["link"]))
#         except sqlite3.IntegrityError:
#             # If job already exists, check for updates
#             cursor.execute("""
#                 SELECT description, link FROM jobs
#                 WHERE title=? AND company=? AND location=?
#             """, (job["title"], job["company"], job["location"]))
#             existing = cursor.fetchone()
#             if existing and (existing[0] != job["description"] or existing[1] != job["link"]):
#                 cursor.execute("""
#                     UPDATE jobs
#                     SET description=?, link=?
#                     WHERE title=? AND company=? AND location=?
#                 """, (job["description"], job["link"], job["title"], job["company"], job["location"]))
#     conn.commit()
#
#
# # -----------------------------
# # Step 4: Filtering
# # -----------------------------
# def filter_jobs(conn, location=None, company=None):
#     cursor = conn.cursor()
#     query = "SELECT title, company, location, description, link FROM jobs WHERE 1=1"
#     params = []
#     if location:
#         query += " AND location=?"
#         params.append(location)
#     if company:
#         query += " AND company=?"
#         params.append(company)
#     cursor.execute(query, params)
#     return cursor.fetchall()
#
#
# # -----------------------------
# # Step 5: Export to CSV
# # -----------------------------
# def export_to_csv(jobs, filename="filtered_jobs.csv"):
#     with open(filename, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
#         writer.writerows(jobs)
#     print(f"Exported {len(jobs)} jobs to {filename}")
#
#
# # -----------------------------
# # Main Execution
# # -----------------------------
# if __name__ == "__main__":
#     # Scrape jobs
#     jobs = scrape_jobs()
#
#     # Setup DB
#     conn = setup_database()
#
#     # Save jobs (incremental + update tracking)
#     save_jobs(conn, jobs)
#
#     # Example filtering
#     filtered = filter_jobs(conn, location="Remote")
#     export_to_csv(filtered, "remote_jobs.csv")
#
#     conn.close()
#
#
# """Task3"""
#
# import requests
# from bs4 import BeautifulSoup
# import json
#
# BASE_URL = "https://www.demoblaze.com/"
# CATEGORY_URL = BASE_URL + "index.html"
#
# def scrape_laptops():
#     laptops = []
#     page = 1
#     while True:
#         # Load laptops category with pagination
#         url = f"{BASE_URL}index.html?page={page}&cat=laptop"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#
#         # Find all product cards
#         items = soup.find_all("div", class_="card-block")
#         if not items:
#             break  # Stop when no more laptops are found
#
#         for item in items:
#             name = item.find("h4", class_="card-title").text.strip()
#             price = item.find("h5").text.strip()
#             description = item.find("p", class_="card-text").text.strip()
#
#             laptops.append({
#                 "name": name,
#                 "price": price,
#                 "description": description
#             })
#
#         page += 1  # Go to next page
#
#     return laptops
#
#
# def save_to_json(data, filename="laptops.json"):
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#     print(f"Saved {len(data)} laptops to {filename}")
#
#
# if __name__ == "__main__":
#     laptops = scrape_laptops()
#     save_to_json(laptops)
