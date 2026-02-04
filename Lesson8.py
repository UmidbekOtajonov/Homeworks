"""Model a Farm"""
# class Animal:
#     def __init__(self, name, age, sound):
#         self.name = name
#         self.age = age
#         self.sound = sound
#
#     def eat(self):
#         print(f"{self.name} is eating.")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping.")
#
#     def make_sound(self):
#         print(f"{self.name} says {self.sound}!")
#
#
# class Cow(Animal):
#     def __init__(self, name, age, milk_production):
#         super().__init__(name, age, "Moo")
#         self.milk_production = milk_production
#
#     def graze(self):
#         print(f"{self.name} is grazing in the field.")
#
#
# class Chicken(Animal):
#     def __init__(self, name, age, egg_count=0):
#         super().__init__(name, age, "Cluck")
#         self.egg_count = egg_count
#
#     def lay_egg(self):
#         self.egg_count += 1
#         print(f"{self.name} laid an egg! Total eggs: {self.egg_count}")
#
#
# class Horse(Animal):
#     def __init__(self, name, age, speed):
#         super().__init__(name, age, "Neigh")
#         self.speed = speed
#
#     def run(self):
#         print(f"{self.name} runs at {self.speed} km/h!")
#
#
# # --- Usage ---
# cow = Cow("Bessie", 5, 20)
# chicken = Chicken("Clucky", 2)
# horse = Horse("Thunder", 7, 60)
#
# cow.make_sound()
# cow.graze()
# chicken.lay_egg()
# horse.run()
#
#
# """Build a Bank Application"""
#
# import json
# import os
#
# class Account:
#     def __init__(self, account_number, name, balance=0):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if amount > self.balance:
#             raise ValueError("Insufficient funds.")
#         self.balance -= amount
#
#     def __str__(self):
#         return f"Account[{self.account_number}] - {self.name}, Balance: {self.balance}"
#
#
# class Bank:
#     def __init__(self, filename="accounts.txt"):
#         self.accounts = {}
#         self.filename = filename
#         self.load_from_file()
#
#     def create_account(self, name, initial_deposit):
#         account_number = str(len(self.accounts) + 1).zfill(5)  # e.g., 00001
#         account = Account(account_number, name, initial_deposit)
#         self.accounts[account_number] = account
#         self.save_to_file()
#         print(f"Account created: {account}")
#
#     def view_account(self, account_number):
#         account = self.accounts.get(account_number)
#         if account:
#             print(account)
#         else:
#             print("Account not found.")
#
#     def deposit(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account:
#             try:
#                 account.deposit(amount)
#                 self.save_to_file()
#                 print(f"Deposited {amount} to {account_number}. New balance: {account.balance}")
#             except ValueError as e:
#                 print(e)
#         else:
#             print("Account not found.")
#
#     def withdraw(self, account_number, amount):
#         account = self.accounts.get(account_number)
#         if account:
#             try:
#                 account.withdraw(amount)
#                 self.save_to_file()
#                 print(f"Withdrew {amount} from {account_number}. New balance: {account.balance}")
#             except ValueError as e:
#                 print(e)
#         else:
#             print("Account not found.")
#
#     def save_to_file(self):
#         with open(self.filename, "w") as f:
#             json.dump({acc_num: vars(acc) for acc_num, acc in self.accounts.items()}, f)
#
#     def load_from_file(self):
#         if os.path.exists(self.filename):
#             with open(self.filename, "r") as f:
#                 data = json.load(f)
#                 for acc_num, acc_data in data.items():
#                     self.accounts[acc_num] = Account(**acc_data)
#







































