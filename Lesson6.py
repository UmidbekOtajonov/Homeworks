# Zero Check Decorator
#
# def check(func):
#     def wrapper(*args):
#         try:
#             result = func(*args)
#             print(f"{func.__name__} muvaffaqiyatli bajarildi.")
#             return result
#         except Exception as e:
#             print(f" Xatolik: {e}")
#             return None
#     return wrapper
#
# @check
# def div(a, b):
#     return a / b
#
# print(div(10, 2))
# print(div(1, 0))
#

#
# """"**Employee Records Manager**"""
# import os
#
# FILENAME = "employees.txt"
#
# # 1. Fayl mavjud bo‘lmasa, yaratamiz
# if not os.path.exists(FILENAME):
#     with open(FILENAME, "w") as f:
#         pass
#
# # --- Funksiyalar ---
# def add_employee():
#     emp_id = input("Employee ID: ")
#     name = input("Name: ")
#     position = input("Position: ")
#     salary = input("Salary: ")
#
#     with open(FILENAME, "a") as f:
#         f.write(f"{emp_id}, {name}, {position}, {salary}\n")
#     print(" Employee qo‘shildi.\n")
#
#
# def view_employees():
#     with open(FILENAME, "r") as f:
#         records = f.readlines()
#         if not records:
#             print(" Hech qanday employee mavjud emas.\n")
#         else:
#             print(" Employee Records:")
#             for record in records:
#                 print(record.strip())
#             print()
#
#
# def search_employee():
#     emp_id = input("Qidirilayotgan Employee ID: ")
#     found = False
#     with open(FILENAME, "r") as f:
#         for line in f:
#             fields = line.strip().split(",")
#             if fields[0] == emp_id:
#                 print(" Employee topildi:", line.strip(), "\n")
#                 found = True
#                 break
#     if not found:
#         print(" Employee topilmadi.\n")
#
#
# def update_employee():
#     emp_id = input("Yangilash uchun Employee ID: ")
#     updated = False
#     with open(FILENAME, "r") as f:
#         records = f.readlines()
#
#     with open(FILENAME, "w") as f:
#         for line in records:
#             fields = line.strip().split(",")
#             if fields[0] == emp_id:
#                 print("Hozirgi ma’lumot:", line.strip())
#                 name = input("Yangi Name: ")
#                 position = input("Yangi Position: ")
#                 salary = input("Yangi Salary: ")
#                 f.write(f"{emp_id}, {name}, {position}, {salary}\n")
#                 updated = True
#             else:
#                 f.write(line)
#
#     if updated:
#         print(" Employee yangilandi.\n")
#     else:
#         print(" Employee topilmadi.\n")
#
#
# def delete_employee():
#     emp_id = input("O‘chirish uchun Employee ID: ")
#     deleted = False
#     with open(FILENAME, "r") as f:
#         records = f.readlines()
#
#     with open(FILENAME, "w") as f:
#         for line in records:
#             fields = line.strip().split(",")
#             if fields[0] == emp_id:
#                 deleted = True
#                 continue
#             f.write(line)
#
#     if deleted:
#         print(" Employee o‘chirildi.\n")
#     else:
#         print(" Employee topilmadi.\n")
#
#
# # --- Menu ---
# def menu():
#     while True:
#         print(" Employee Records Manager:")
#         print("1. Add new employee record")
#         print("2. View all employee records")
#         print("3. Search for an employee by Employee ID")
#         print("4. Update an employee's information")
#         print("5. Delete an employee record")
#         print("6. Exit")
#
#         choice = input("Tanlovingiz (1-6): ")
#
#         if choice == "1":
#             add_employee()
#         elif choice == "2":
#             view_employees()
#         elif choice == "3":
#             search_employee()
#         elif choice == "4":
#             update_employee()
#         elif choice == "5":
#             delete_employee()
#         elif choice == "6":
#             print(" Dastur tugadi.")
#             break
#         else:
#             print("⚠ Noto‘g‘ri tanlov.\n")
#
#
# # --- Dastur ishga tushirish ---
# menu()

#
# """Word Frequency Counter"""
# import os
# import string
# from collections import Counter
#
# def get_text_from_file(filename="sample.txt"):
#     # If file doesn't exist, prompt user to create it
#     if not os.path.exists(filename):
#         print(f"'{filename}' not found. Please type a paragraph to create it:")
#         user_input = input("Enter text: ")
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(user_input)
#
#     # Read file content
#     with open(filename, "r", encoding="utf-8") as f:
#         return f.read()
#
#
# def clean_and_split_text(text):
#     # Convert to lowercase
#     text = text.lower()
#     # Remove punctuation
#     text = text.translate(str.maketrans("", "", string.punctuation))
#     # Split into words
#     return text.split()
#
#
# def count_word_frequency(words):
#     return Counter(words)
#
#
# def save_report(total_words, common_words, filename="word_count_report.txt"):
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("Word Count Report\n")
#         f.write(f"Total Words: {total_words}\n")
#         f.write("Top 5 Words:\n")
#         for word, count in common_words:
#             f.write(f"{word} - {count}\n")
#
#
# def main():
#     # Step 1: Get text
#     text = get_text_from_file("sample.txt")
#
#     # Step 2: Clean and split
#     words = clean_and_split_text(text)
#
#     # Step 3: Count frequency
#     word_counts = count_word_frequency(words)
#
#     # Step 4: Output results
#     total_words = len(words)
#     common_words = word_counts.most_common(5)
#
#     print(f"Total words: {total_words}")
#     print("Top 5 most common words:")
#     for word, count in common_words:
#         print(f"{word} - {count} times")
#
#     # Step 5: Save report
#     save_report(total_words, common_words)
#
#
# if __name__ == "__main__":
#     main()
#
#
# """Bonus task"""
# import os
# import string
# from collections import Counter
#
#
# def get_text_from_file(filename="sample.txt"):
#     # If file doesn't exist, prompt user to create it
#     if not os.path.exists(filename):
#         print(f"'{filename}' not found. Please type a paragraph to create it:")
#         user_input = input("Enter text: ")
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(user_input)
#
#     # Read file content efficiently
#     with open(filename, "r", encoding="utf-8") as f:
#         return f.read()
#
#
# def clean_and_split_text(text):
#     # Convert to lowercase
#     text = text.lower()
#     # Remove punctuation
#     text = text.translate(str.maketrans("", "", string.punctuation))
#     # Split into words
#     return text.split()
#
#
# def count_word_frequency(words):
#     return Counter(words)
#
#
# def save_report(total_words, common_words, filename="word_count_report.txt"):
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("Word Count Report\n")
#         f.write(f"Total Words: {total_words}\n")
#         f.write("Top Words:\n")
#         for word, count in common_words:
#             f.write(f"{word} - {count}\n")
#
#
# def main():
#     # Step 1: Get text
#     text = get_text_from_file("sample.txt")
#
#     # Step 2: Clean and split
#     words = clean_and_split_text(text)
#
#     # Step 3: Count frequency
#     word_counts = count_word_frequency(words)
#
#     # Step 4: Ask user how many top words to display
#     try:
#         n = int(input("How many top common words would you like to see? "))
#     except ValueError:
#         print("Invalid input. Defaulting to top 5 words.")
#         n = 5
#
#     # Step 5: Output results
#     total_words = len(words)
#     common_words = word_counts.most_common(n)
#
#     print(f"Total words: {total_words}")
#     print(f"Top {n} most common words:")
#     for word, count in common_words:
#         print(f"{word} - {count} times")
#
#     # Step 6: Save report
#     save_report(total_words, common_words)
#
#
# if __name__ == "__main__":
#     main()






