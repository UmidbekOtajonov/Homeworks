from datetime import date

name = input("Enter your name: ")
birthyear = int(input("Enter your birthyear: "))
age = date.today().year - birthyear
print("Your age is:", age)