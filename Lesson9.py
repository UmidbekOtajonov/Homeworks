# """Task 1: Create a Library Management System with Custom Exceptions"""
# # -------------------------------
# # Custom Exceptions
# # -------------------------------
# class BookNotFoundException(Exception):
#     """Raised when the requested book is not found in the library."""
#     pass
#
# class BookAlreadyBorrowedException(Exception):
#     """Raised when the requested book is already borrowed."""
#     pass
#
# class MemberLimitExceededException(Exception):
#     """Raised when a member tries to borrow more than 3 books."""
#     pass
#
#
# # -------------------------------
# # Book Class
# # -------------------------------
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
#
#     def __str__(self):
#         status = "Borrowed" if self.is_borrowed else "Available"
#         return f"'{self.title}' by {self.author} - {status}"
#
#
# # -------------------------------
# # Member Class
# # -------------------------------
# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
#
#     def borrow_book(self, book):
#         if len(self.borrowed_books) >= 3:
#             raise MemberLimitExceededException(
#                 f"{self.name} cannot borrow more than 3 books."
#             )
#         if book.is_borrowed:
#             raise BookAlreadyBorrowedException(
#                 f"The book '{book.title}' is already borrowed."
#             )
#         book.is_borrowed = True
#         self.borrowed_books.append(book)
#
#     def return_book(self, book):
#         if book in self.borrowed_books:
#             book.is_borrowed = False
#             self.borrowed_books.remove(book)
#
#     def __str__(self):
#         borrowed_titles = [book.title for book in self.borrowed_books]
#         return f"Member: {self.name}, Borrowed: {borrowed_titles}"
#
#
# # -------------------------------
# # Library Class
# # -------------------------------
# class Library:
#     def __init__(self):
#         self.books = []
#         self.members = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def add_member(self, member):
#         self.members.append(member)
#
#     def find_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 return book
#         raise BookNotFoundException(f"Book '{title}' not found in library.")
#
#     def borrow_book(self, member_name, book_title):
#         member = next((m for m in self.members if m.name == member_name), None)
#         if not member:
#             print(f"Member '{member_name}' not found.")
#             return
#
#         book = self.find_book(book_title)
#         member.borrow_book(book)
#         print(f"{member.name} borrowed '{book.title}'.")
#
#     def return_book(self, member_name, book_title):
#         member = next((m for m in self.members if m.name == member_name), None)
#         if not member:
#             print(f"Member '{member_name}' not found.")
#             return
#
#         book = self.find_book(book_title)
#         member.return_book(book)
#         print(f"{member.name} returned '{book.title}'.")
#
#     def show_books(self):
#         for book in self.books:
#             print(book)
#
#     def show_members(self):
#         for member in self.members:
#             print(member)
#
#
# # -------------------------------
# # Testing the System
# # -------------------------------
# if __name__ == "__main__":
#     # Create library
#     library = Library()
#
#     # Add books
#     library.add_book(Book("1984", "George Orwell"))
#     library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
#     library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
#
#     # Add members
#     alice = Member("Alice")
#     bob = Member("Bob")
#     library.add_member(alice)
#     library.add_member(bob)
#
#     # Show initial state
#     print("\n--- Initial Library State ---")
#     library.show_books()
#     library.show_members()
#
#     # Borrowing books
#     print("\n--- Borrowing Books ---")
#     try:
#         library.borrow_book("Alice", "1984")
#         library.borrow_book("Bob", "To Kill a Mockingbird")
#         library.borrow_book("Alice", "The Great Gatsby")
#     except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
#         print("Error:", e)
#
#     # Trying to borrow a non-existent book
#     print("\n--- Exception: Book Not Found ---")
#     try:
#         library.borrow_book("Alice", "Invisible Man")
#     except Exception as e:
#         print("Error:", e)
#
#     # Trying to borrow an already borrowed book
#     print("\n--- Exception: Book Already Borrowed ---")
#     try:
#         library.borrow_book("Bob", "1984")
#     except Exception as e:
#         print("Error:", e)
#
#     # Exceeding member limit
#     print("\n--- Exception: Member Limit Exceeded ---")
#     try:
#         library.borrow_book("Alice", "To Kill a Mockingbird")  # Alice already has 2 books
#         library.borrow_book("Alice", "Another Book")  # This should exceed limit
#     except Exception as e:
#         print("Error:", e)
#
#     # Returning books
#     print("\n--- Returning Books ---")
#     library.return_book("Alice", "1984")
#     library.return_book("Bob", "To Kill a Mockingbird")
#
#     # Final state
#     print("\n--- Final Library State ---")
#     library.show_books()
#     library.show_members()
#
#
# """Task 2: Student Grades Management"""
# import csv
# from collections import defaultdict
#
# # -------------------------------
# # Step 1: Faylni yaratish va ma'lumot yozish
# # -------------------------------
# with open("grades.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     # Sarlavha yozamiz
#     writer.writerow(["Name", "Subject", "Grade"])
#     # Ma'lumotlar yozamiz
#     writer.writerow(["Alice", "Math", 85])
#     writer.writerow(["Bob", "Science", 78])
#     writer.writerow(["Carol", "Math", 92])
#     writer.writerow(["Dave", "History", 74])
#
# print(" grades.csv fayli yaratildi va ma'lumot yozildi.")
#
# # -------------------------------
# # Step 2: Fayldan o‘qish
# # -------------------------------
# grades_data = []
# with open("grades.csv", mode="r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         row["Grade"] = int(row["Grade"])  # int ga aylantiramiz
#         grades_data.append(row)
#
# # -------------------------------
# # Step 3: O‘rtacha bahoni hisoblash
# # -------------------------------
# subject_totals = defaultdict(list)
# for entry in grades_data:
#     subject_totals[entry["Subject"]].append(entry["Grade"])
#
# average_grades = {subject: sum(grades) / len(grades)
#                   for subject, grades in subject_totals.items()}
#
# # -------------------------------
# # Step 4: Yangi faylga yozish
# # -------------------------------
# with open("average_grades.csv", mode="w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Subject", "Average Grade"])
#     for subject, avg in average_grades.items():
#         writer.writerow([subject, round(avg, 2)])
#
# print(" average_grades.csv fayli yaratildi.")
#
# """Task 3: JSON Handling"""
# import json
# import csv
#
# # -------------------------------
# # Step 1: Faylni yaratish va yozish
# # -------------------------------
# initial_tasks = [
#     {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
#     {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
#     {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
# ]
#
# with open("tasks.json", "w") as file:
#     json.dump(initial_tasks, file, indent=4)
#
# print(" tasks.json fayli yaratildi va ma'lumot yozildi.")
#
#
# # -------------------------------
# # Step 2: Fayldan o‘qish
# # -------------------------------
# def load_tasks(filename="tasks.json"):
#     with open(filename, "r") as file:
#         return json.load(file)
#
#
# # -------------------------------
# # Step 3: Vazifalarni ko‘rsatish
# # -------------------------------
# def display_tasks(tasks):
#     print("\n--- All Tasks ---")
#     for task in tasks:
#         print(f"ID: {task['id']}, Task: {task['task']}, "
#               f"Completed: {task['completed']}, Priority: {task['priority']}")
#
#
# # -------------------------------
# # Step 4: O‘zgartirish va saqlash
# # -------------------------------
# def save_tasks(tasks, filename="tasks.json"):
#     with open(filename, "w") as file:
#         json.dump(tasks, file, indent=4)
#     print(" Changes saved to tasks.json")
#
#
# # -------------------------------
# # Step 5: Statistikani hisoblash
# # -------------------------------
# def calculate_stats(tasks):
#     total = len(tasks)
#     completed = sum(1 for t in tasks if t["completed"])
#     pending = total - completed
#     avg_priority = sum(t["priority"] for t in tasks) / total if total > 0 else 0
#
#     print("\n--- Task Statistics ---")
#     print(f"Total tasks: {total}")
#     print(f"Completed tasks: {completed}")
#     print(f"Pending tasks: {pending}")
#     print(f"Average priority: {round(avg_priority, 2)}")
#
#
# # -------------------------------
# # Step 6: JSON → CSV konvertatsiya
# # -------------------------------
# def convert_json_to_csv(json_file="tasks.json", csv_file="tasks.csv"):
#     tasks = load_tasks(json_file)
#     with open(csv_file, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["ID", "Task", "Completed", "Priority"])
#         for task in tasks:
#             writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
#     print(f" {csv_file} fayli yaratildi.")
#
#
# # -------------------------------
# # Test qilish
# # -------------------------------
# if __name__ == "__main__":
#     tasks = load_tasks()
#     display_tasks(tasks)
#     calculate_stats(tasks)
#
#     # Misol uchun: 1-vazifani bajarilgan deb belgilaymiz
#     tasks[0]["completed"] = True
#     save_tasks(tasks)
#
#     # JSON → CSV konvertatsiya
#     convert_json_to_csv()



