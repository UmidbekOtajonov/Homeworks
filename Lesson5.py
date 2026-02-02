# task1
# def convert_cel_to_far(celsius: float) -> float:
#     """Convert Celsius to Fahrenheit"""
#     return celsius * 9/5 + 32
#
# def convert_far_to_cel(fahrenheit: float) -> float:
#     """Convert Fahrenheit to Celsius"""
#     return (fahrenheit - 32) * 5/9
#
#
# """Prompt user for Fahrenheit"""
# far = float(input("Enter a temperature in degrees F: "))
# cel = convert_far_to_cel(far)
# print(f"{far} degrees F = {round(cel, 2)} degrees C")
#
# """Prompt user for Celsius"""
# cel = float(input("\nEnter a temperature in degrees C: "))
# far = convert_cel_to_far(cel)
# print(f"{cel} degrees C = {round(far, 2)} degrees F")
#
#
# task2
# def invest(amount, rate, years):
#     """Track investment growth over time"""
#     for year in range(1, years + 1):
#         amount = amount * (1 + rate)
#         print(f"year {year}: ${amount:.2f}")
#
# principal = float(input("Enter the initial amount: "))
# annual_rate = float(input("Enter the annual rate of return (as decimal, e.g. 0.05 for 5%): "))
# num_years = int(input("Enter the number of years: "))
# invest(principal, annual_rate, num_years)
#
# task3
#
# n = int(input("Enter a positive integer: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(f"{i} is a factor of {n}")
#
# task4
#
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]
#
# def enrollment_stats(universities):
#     """Return two lists: enrollments and tuitions"""
#     enrollments = []
#     tuitions = []
#     for uni in universities:
#         enrollments.append(uni[1])
#         tuitions.append(uni[2])
#     return enrollments, tuitions
#
# def mean(values):
#     """Return mean of list"""
#     return sum(values) / len(values)
# def median(values):
#     """Return median of list"""
#     sorted_values = sorted(values)
#     n = len(sorted_values)
#     mid = n // 2
#     if n % 2 == 0:  # even length
#         return (sorted_values[mid - 1] + sorted_values[mid]) / 2
#     else:  # odd length
#         return sorted_values[mid]
#
#
# enrollments, tuitions = enrollment_stats(universities)
#
# total_students = sum(enrollments)
# total_tuition = sum(tuitions)
#
# student_mean = mean(enrollments)
# student_median = median(enrollments)
#
# tuition_mean = mean(tuitions)
# tuition_median = median(tuitions)
#
# print("******************************")
# print(f"Total students: {total_students:,}")
# print(f"Total tuition: $ {total_tuition:,}\n")
# print(f"Student mean: {student_mean:,.2f}")
# print(f"Student median: {student_median:,}\n")
# print(f"Tuition mean: $ {tuition_mean:,.2f}")
# print(f"Tuition median: $ {tuition_median:,}")
# print("******************************")
#
# task5
#
# def is_prime(n: int) -> bool:
#     """Return True if n is a prime number, else False."""
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


