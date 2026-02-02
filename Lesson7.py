# """Generalized `Vector` Class"""
# import math
#
# class Vector:
#     def __init__(self, *components):
#         if not components:
#             raise ValueError("Vector must have at least one component")
#         self.components = tuple(components)
#
#     def __str__(self):
#         return f"Vector{self.components}"
#
#     def __repr__(self):
#         return f"Vector{self.components}"
#
#     def __len__(self):
#         return len(self.components)
#
#     # Qo‘shish
#     def __add__(self, other):
#         if len(self) != len(other):
#             raise ValueError("Vectors must have the same dimension for addition")
#         return Vector(*(a + b for a, b in zip(self.components, other.components)))
#
#     # Ayirish
#     def __sub__(self, other):
#         if len(self) != len(other):
#             raise ValueError("Vectors must have the same dimension for subtraction")
#         return Vector(*(a - b for a, b in zip(self.components, other.components)))
#
#     # Dot product yoki scalar multiplication
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):  # Scalar multiplication
#             return Vector(*(a * other for a in self.components))
#         elif isinstance(other, Vector):      # Dot product
#             if len(self) != len(other):
#                 raise ValueError("Vectors must have the same dimension for dot product")
#             return sum(a * b for a, b in zip(self.components, other.components))
#         else:
#             raise TypeError("Unsupported operand type for *")
#
#     # Scalar multiplication (chapdan)
#     def __rmul__(self, other):
#         return self * other
#
#     # Magnitude (uzunlik)
#     def magnitude(self):
#         return math.sqrt(sum(a ** 2 for a in self.components))
#
#     # Normalization (unit vector)
#     def normalize(self):
#         mag = self.magnitude()
#         if mag == 0:
#             raise ValueError("Cannot normalize zero vector")
#         return Vector(*(a / mag for a in self.components))

#
# """Employee Records Manager (OOP Version)"""
# import os
#
# class Employee:
#     def __init__(self, employee_id, name, position, salary):
#         self.employee_id = str(employee_id)
#         self.name = name
#         self.position = position
#         self.salary = float(salary)
#
#     def __str__(self):
#         return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
#
#
# class EmployeeManager:
#     FILE_NAME = "employees.txt"
#
#     def __init__(self):
#         # Fayl mavjud bo‘lmasa, yaratib qo‘yish
#         if not os.path.exists(self.FILE_NAME):
#             with open(self.FILE_NAME, "w") as f:
#                 pass
#
#     def add_employee(self, employee):
#         # Unikal ID tekshirish
#         if self.search_employee(employee.employee_id):
#             print("❌ Employee ID already exists!")
#             return
#         with open(self.FILE_NAME, "a") as f:
#             f.write(str(employee) + "\n")
#         print("✅ Employee added successfully!")
#
#     def view_all_employees(self, sort_by=None):
#         with open(self.FILE_NAME, "r") as f:
#             records = [line.strip() for line in f if line.strip()]
#
#         if not records:
#             print("⚠️ No employee records found.")
#             return
#
#         employees = []
#         for rec in records:
#             emp_id, name, position, salary = rec.split(", ")
#             employees.append(Employee(emp_id, name, position, salary))
#
#         # Sort qilish (bonus challenge)
#         if sort_by == "name":
#             employees.sort(key=lambda e: e.name)
#         elif sort_by == "salary":
#             employees.sort(key=lambda e: e.salary)
#
#         print("\n📋 Employee Records:")
#         for emp in employees:
#             print(emp)
#
#     def search_employee(self, employee_id):
#         with open(self.FILE_NAME, "r") as f:
#             for line in f:
#                 if line.startswith(str(employee_id) + ","):
#                     emp_id, name, position, salary = line.strip().split(", ")
#                     return Employee(emp_id, name, position, salary)
#         return None
#
#     def update_employee(self, employee_id, name=None, position=None, salary=None):
#         found = False
#         with open(self.FILE_NAME, "r") as f:
#             records = [line.strip() for line in f if line.strip()]
#
#         new_records = []
#         for rec in records:
#             emp_id, emp_name, emp_position, emp_salary = rec.split(", ")
#             if emp_id == str(employee_id):
#                 found = True
#                 emp_name = name if name else emp_name
#                 emp_position = position if position else emp_position
#                 emp_salary = salary if salary else emp_salary
#                 new_records.append(f"{emp_id}, {emp_name}, {emp_position}, {emp_salary}")
#             else:
#                 new_records.append(rec)
#
#         if found:
#             with open(self.FILE_NAME, "w") as f:
#                 for rec in new_records:
#                     f.write(rec + "\n")
#             print("✅ Employee updated successfully!")
#         else:
#             print("❌ Employee not found!")
#
#     def delete_employee(self, employee_id):
#         found = False
#         with open(self.FILE_NAME, "r") as f:
#             records = [line.strip() for line in f if line.strip()]
#
#         new_records = [rec for rec in records if not rec.startswith(str(employee_id) + ",")]
#
#         if len(new_records) != len(records):
#             found = True
#             with open(self.FILE_NAME, "w") as f:
#                 for rec in new_records:
#                     f.write(rec + "\n")
#             print("✅ Employee deleted successfully!")
#         else:
#             print("❌ Employee not found!")
#
#     def menu(self):
#         while True:
#             print("\nWelcome to the Employee Records Manager!")
#             print("1. Add new employee record")
#             print("2. View all employee records")
#             print("3. Search for an employee by Employee ID")
#             print("4. Update an employee's information")
#             print("5. Delete an employee record")
#             print("6. Exit")
#
#             choice = input("Enter your choice: ")
#
#             if choice == "1":
#                 emp_id = input("Enter Employee ID: ")
#                 name = input("Enter Name: ")
#                 position = input("Enter Position: ")
#                 salary = input("Enter Salary: ")
#                 employee = Employee(emp_id, name, position, salary)
#                 self.add_employee(employee)
#
#             elif choice == "2":
#                 sort_choice = input("Sort by (name/salary/none): ").lower()
#                 sort_by = sort_choice if sort_choice in ["name", "salary"] else None
#                 self.view_all_employees(sort_by)
#
#             elif choice == "3":
#                 emp_id = input("Enter Employee ID to search: ")
#                 employee = self.search_employee(emp_id)
#                 if employee:
#                     print("✅ Employee Found:")
#                     print(employee)
#                 else:
#                     print("❌ Employee not found!")
#
#             elif choice == "4":
#                 emp_id = input("Enter Employee ID to update: ")
#                 name = input("Enter new Name (leave blank to keep current): ") or None
#                 position = input("Enter new Position (leave blank to keep current): ") or None
#                 salary = input("Enter new Salary (leave blank to keep current): ") or None
#                 self.update_employee(emp_id, name, position, salary)
#
#             elif choice == "5":
#                 emp_id = input("Enter Employee ID to delete: ")
#                 self.delete_employee(emp_id)
#
#             elif choice == "6":
#                 print("👋 Goodbye!")
#                 break
#             else:
#                 print("⚠️ Invalid choice, please try again.")
#
#
# """To-Do Application"""
#
# import csv
# import json
# import os
#
# # -------------------------------
# # Task Class
# # -------------------------------
# class Task:
#     def __init__(self, task_id, title, description, due_date=None, status="Pending"):
#         self.task_id = str(task_id)
#         self.title = title
#         self.description = description
#         self.due_date = due_date
#         self.status = status
#
#     def __str__(self):
#         return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"
#
#     def to_dict(self):
#         return {
#             "task_id": self.task_id,
#             "title": self.title,
#             "description": self.description,
#             "due_date": self.due_date,
#             "status": self.status
#         }
#
#
# # -------------------------------
# # Storage Strategy Interface
# # -------------------------------
# class StorageStrategy:
#     def save(self, tasks, filename):
#         raise NotImplementedError
#
#     def load(self, filename):
#         raise NotImplementedError
#
#
# # -------------------------------
# # CSV Storage Implementation
# # -------------------------------
# class CSVStorage(StorageStrategy):
#     def save(self, tasks, filename):
#         with open(filename, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
#             writer.writeheader()
#             for task in tasks:
#                 writer.writerow(task.to_dict())
#
#     def load(self, filename):
#         tasks = []
#         if os.path.exists(filename):
#             with open(filename, "r") as f:
#                 reader = csv.DictReader(f)
#                 for row in reader:
#                     tasks.append(Task(**row))
#         return tasks
#
#
# # -------------------------------
# # JSON Storage Implementation
# # -------------------------------
# class JSONStorage(StorageStrategy):
#     def save(self, tasks, filename):
#         with open(filename, "w") as f:
#             json.dump([task.to_dict() for task in tasks], f, indent=4)
#
#     def load(self, filename):
#         tasks = []
#         if os.path.exists(filename):
#             with open(filename, "r") as f:
#                 data = json.load(f)
#                 for row in data:
#                     tasks.append(Task(**row))
#         return tasks
#
#
# # -------------------------------
# # Task Manager
# # -------------------------------
# class TaskManager:
#     def __init__(self, storage_strategy, filename):
#         self.storage = storage_strategy
#         self.filename = filename
#         self.tasks = self.storage.load(self.filename)
#
#     def add_task(self, task):
#         if any(t.task_id == task.task_id for t in self.tasks):
#             print("❌ Task ID already exists!")
#             return
#         self.tasks.append(task)
#         print("✅ Task added successfully!")
#
#     def view_tasks(self):
#         if not self.tasks:
#             print("⚠️ No tasks found.")
#             return
#         print("\n📋 Tasks:")
#         for task in self.tasks:
#             print(task)
#
#     def update_task(self, task_id, **kwargs):
#         for task in self.tasks:
#             if task.task_id == str(task_id):
#                 task.title = kwargs.get("title", task.title)
#                 task.description = kwargs.get("description", task.description)
#                 task.due_date = kwargs.get("due_date", task.due_date)
#                 task.status = kwargs.get("status", task.status)
#                 print("✅ Task updated successfully!")
#                 return
#         print("❌ Task not found!")
#
#     def delete_task(self, task_id):
#         before_count = len(self.tasks)
#         self.tasks = [t for t in self.tasks if t.task_id != str(task_id)]
#         if len(self.tasks) < before_count:
#             print("✅ Task deleted successfully!")
#         else:
#             print("❌ Task not found!")
#
#     def filter_tasks(self, status):
#         filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
#         if not filtered:
#             print(f"⚠️ No tasks with status '{status}' found.")
#             return
#         print(f"\n📋 Tasks with status '{status}':")
#         for task in filtered:
#             print(task)
#
#     def save_tasks(self):
#         self.storage.save(self.tasks, self.filename)
#         print("💾 Tasks saved successfully!")
#
#     def load_tasks(self):
#         self.tasks = self.storage.load(self.filename)
#         print("📂 Tasks loaded successfully!")
#
#
# # -------------------------------
# # Menu System
# # -------------------------------
# def menu():
#     # Choose storage format (CSV or JSON)
#     choice = input("Choose storage format (csv/json): ").lower()
#     if choice == "csv":
#         storage = CSVStorage()
#         filename = "tasks.csv"
#     else:
#         storage = JSONStorage()
#         filename = "tasks.json"
#
#     manager = TaskManager(storage, filename)
#
#     while True:
#         print("\nWelcome to the To-Do Application!")
#         print("1. Add a new task")
#         print("2. View all tasks")
#         print("3. Update a task")
#         print("4. Delete a task")
#         print("5. Filter tasks by status")
#         print("6. Save tasks")
#         print("7. Load tasks")
#         print("8. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             task_id = input("Enter Task ID: ")
#             title = input("Enter Title: ")
#             description = input("Enter Description: ")
#             due_date = input("Enter Due Date (YYYY-MM-DD): ") or None
#             status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
#             manager.add_task(Task(task_id, title, description, due_date, status))
#
#         elif choice == "2":
#             manager.view_tasks()
#
#         elif choice == "3":
#             task_id = input("Enter Task ID to update: ")
#             title = input("Enter new Title (leave blank to keep current): ") or None
#             description = input("Enter new Description (leave blank to keep current): ") or None
#             due_date = input("Enter new Due Date (leave blank to keep current): ") or None
#             status = input("Enter new Status (leave blank to keep current): ") or None
#             manager.update_task(task_id, title=title, description=description, due_date=due_date, status=status)
#
#         elif choice == "4":
#             task_id = input("Enter Task ID to delete: ")
#             manager.delete_task(task_id)
#
#         elif choice == "5":
#             status = input("Enter status to filter by: ")
#             manager.filter_tasks(status)
#
#         elif choice == "6":
#             manager.save_tasks()
#
#         elif choice == "7":
#             manager.load_tasks()
#
#         elif choice == "8":
#             print("👋 Goodbye!")
#             break
#
#         else:
#             print("⚠️ Invalid choice, please try again.")
#
#
# # Run the menu
# if __name__ == "__main__":
#     menu()








