# """Task1"""
# import sqlite3
#
# # 1. Database Creation
# with sqlite3.connect("roster.db") as conn:
#     cursor = conn.cursor()
#
#     # Agar jadval bo‘lsa, o‘chirib tashlaymiz
#     cursor.execute("DROP TABLE IF EXISTS Roster")
#
#     # Yangi jadval yaratamiz
#     cursor.execute("""
#                    CREATE TABLE Roster
#                    (
#                        Name    TEXT,
#                        Species TEXT,
#                        Age     INTEGER
#                    )
#                    """)
#
#     # 2. Insert Data
#     roster_data = [
#         ("Benjamin Sisko", "Human", 40),
#         ("Jadzia Dax", "Trill", 300),
#         ("Kira Nerys", "Bajoran", 29)
#     ]
#     cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", roster_data)
#
#     # 3. Update Data
#     cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
#
#     # 4. Query Data (Species = Bajoran)
#     print("Bajoranlar:")
#     cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
#     for row in cursor.fetchall():
#         print(row)
#
#     # 5. Delete Data (Age > 100)
#     cursor.execute("DELETE FROM Roster WHERE Age > 100")
#
#     # 6. Bonus Task: Add Rank column
#     cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
#
#     # Ranklarni yangilash
#     ranks = [
#         ("Captain", "Benjamin Sisko"),
#         ("Lieutenant", "Ezri Dax"),
#         ("Major", "Kira Nerys")
#     ]
#     for rank, name in ranks:
#         cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
#
#     # 7. Advanced Query: Sort by Age DESC
#     print("\nYosh bo‘yicha tartiblangan (DESC):")
#     cursor.execute("SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC")
#     for row in cursor.fetchall():
#         print(row)
#
#     conn.commit()
#
#
# """Task2"""
#
# import sqlite3
#
# # 1. Database Creation
# with sqlite3.connect("library.db") as conn:
#     cursor = conn.cursor()
#
#     # Agar jadval bo‘lsa, o‘chirib tashlaymiz
#     cursor.execute("DROP TABLE IF EXISTS Books")
#
#     # Yangi jadval yaratamiz
#     cursor.execute("""
#                    CREATE TABLE Books
#                    (
#                        Title          TEXT,
#                        Author         TEXT,
#                        Year_Published INTEGER,
#                        Genre          TEXT
#                    )
#                    """)
#
#     # 2. Insert Data
#     books_data = [
#         ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
#         ("1984", "George Orwell", 1949, "Dystopian"),
#         ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
#     ]
#     cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books_data)
#
#     # 3. Update Data (1984 -> 1950)
#     cursor.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))
#
#     # 4. Query Data (Genre = Dystopian)
#     print(" Dystopian janridagi kitoblar:")
#     cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
#     for row in cursor.fetchall():
#         print(row)
#
#     # 5. Delete Data (Year_Published < 1950)
#     cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
#
#     # 6. Bonus Task: Add Rating column
#     cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
#
#     ratings = [
#         (4.8, "To Kill a Mockingbird"),
#         (4.7, "1984"),
#         (4.5, "The Great Gatsby")
#     ]
#     for rating, title in ratings:
#         cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
#
#     # 7. Advanced Query: Sort by Year_Published ASC
#     print("\n Kitoblar yil bo‘yicha tartiblangan (ASC):")
#     cursor.execute("SELECT Title, Author, Year_Published, Genre, Rating FROM Books ORDER BY Year_Published ASC")
#     for row in cursor.fetchall():
#         print(row)
#
#     conn.commit()
