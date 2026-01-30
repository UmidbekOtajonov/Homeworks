# Questions:
#
# program1
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# program2
# row = 5
# for i in range(1, row + 1, 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")
#
# program3
# s = 0
# n = int(input("Enter number "))
# for i in range(1, n + 1, 1):
#     s += i
# print("\n")
# print("Sum is: ", s)
#
# program4
# n = 2
# for i in range(1, 11, 1):
#     product = n * i
#     print(product)
#
# program5
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item % 5 == 0:
#         print(item)
#
# program6
# num = 75878
# count = 0
# while num != 0:
#     num = num // 10
#     count = count + 1
# print("Total digits are:", count)
#
# program7
# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()
#
# program8
# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item)
#
# program9
# for num in range(-10, 0, 1):
#     print(num)
#
# program10
# for i in range(5):
#     print(i)
# else:
#     print("Done!")
#
# program11
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
#
# program12
# num1, num2 = 0, 1
# print("Fibonacci sequence:")
# for i in range(10):
#     print(num1, end="  ")
#     res = num1 + num2
#     num1 = num2
#     num2 = res
#
# program13
# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)
#
# program14
# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)
#
# program15
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#     print(i, end=" ")
#
# program16
# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))
#
# program17
# terms = 5
# num = 2
# sum_seq = 0
# for i in range(0, terms):
#     print(num, end="+")
#     sum_seq += num
#     # calculate the next term
#     num = num * 10 + 2
# print("\nSum of above series is:", sum_seq)
#
# program18
# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")
#
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")
#
# program19
# for i in range(1, 11):
#   print('multiplication table of:', i)
#   for j in range(1, 11):
#     print(f" {i * j}", end="")
#   print()
#
# program20
# def print_alternate_pattern(rows):
#     num = 1
#     for i in range(1, rows + 1):
#         if i % 2 != 0:
#             for x in range(num, num + i):
#               print(x, end=' ')
#             print()
#         else:
#             for y in range(num + i - 1, num - 1, -1):
#               print(y, end=' ')
#             print()
#         num += i
# print_alternate_pattern(5)
#
# program21
# def flatten_list(nested_list):
#     flat_list = []
#     for element in nested_list:
#         if isinstance(element, list):
#             for item in element:
#                 flat_list.append(item)
#         else:
#             flat_list.append(element)
#     return flat_list
#
#
# questions2
# Difference between continue and break in Python
# continue statement
# Skips the rest of the code inside the current loop iteration.
# The loop does not stop; it moves directly to the next iteration.
# break statement
# Immediately terminates the entire loop.
#
# question3
# Difference between for loop and while loop in Python
# for loop
# Used when you want to iterate over a sequence (like a list, tuple, string, or range).
# The number of iterations is usually known or finite.
# while loop
# Used when you want to repeat a block of code until a condition becomes False.
# The number of iterations is often unknown beforehand.
#
# questions4.
# How to Implement a Nested for Loop System in Python
# A nested loop means placing one loop inside another.
# The outer loop runs first, and for each iteration of the outer loop, the inner loop runs completely.
# This is useful for working with grids, tables, matrices, or combinations.
#
#
# Homewors1
#
# list1 = set([1, 1, 2])
# list2 = set([2, 3, 4])
# print(list(list1 ^ list2))
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1 = set(list1)
# list2 = set(list2)
# print(list(list1 | list2))
#
# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]
# temp_list2 = list2.copy()
# result = []
# for item in list1:
#     if item in temp_list2:
#         temp_list2.remove(item)
#     else:
#         result.append(item)
# result.extend(temp_list2)
# print(result)
#
# Homeworks2
# n = 5
# for i in range(1, n):
#     print(i * i)

# Homeworks3
# txt = "hello"
# vowels = ['a', 'e', 'i', 'o', 'u']
# new = ""
# i = 0
# for x in txt:
#     i = i + 1
#     if i %3 == 0 and x not in vowels:
#         new += x
#         if len(txt) != i:
#             new += "_"
#         vowels.append(x)
#     else:
#         new += x
# print(new)
#
# Homeworks4
# import random
#
# def play_game():
#     number = random.randint(1, 100)
#     attempts = 10
#     print("Guess the number between 1 and 100. You have 10 attempts!")
#     for attempt in range(1, attempts + 1):
#         guess = int(input(f"Attempt {attempt}: Enter your guess: "))
#         if guess > number:
#             print("Too high!")
#         elif guess < number:
#             print("Too low!")
#         else:
#             print("You guessed it right!")
#             return
#
#     print("You lost. Want to play again? ")
#     choice = input("Enter Y/YES/y/yes/ok to play again: ")
#     if choice.lower() in ['y', 'yes', 'ok']:
#         play_game()
# play_game()
#
# Homeworks5
# password = input("Enter your password: ")
# if len(password) < 8:
#     print("Password is too short.")
# # Check uppercase
# elif not any(char.isupper() for char in password):
#     print("Password must contain an uppercase letter.")
# else:
#     print("Password is strong.")
#
# Homeworks6
# for num in range(2, 101):  # start from 2 because 1 is not prime
#     is_prime = True
#     for divisor in range(2, num):
#         if num % divisor == 0:
#             is_prime = False
#             break  # not prime, exit inner loop
#     if is_prime:
#         print(num)
#
# Homeworks7
# import random
#
# def play_game():
#     choices = ["rock", "paper", "scissors"]
#     player_score = 0
#     computer_score = 0
#
#     print("Welcome to Rock, Paper, Scissors!")
#     print("First to 5 points wins the match.")
#
#     while player_score < 5 and computer_score < 5:
#         player_choice = input("Enter rock, paper, or scissors: ").lower()
#
#         if player_choice not in choices:
#             print("Invalid choice. Try again.")
#             continue
#
#         computer_choice = random.choice(choices)
#         print(f"Computer chose: {computer_choice}")
#
#         if player_choice == computer_choice:
#             print("It's a tie!")
#         elif (player_choice == "rock" and computer_choice == "scissors") or \
#              (player_choice == "paper" and computer_choice == "rock") or \
#              (player_choice == "scissors" and computer_choice == "paper"):
#             print("You win this round!")
#             player_score += 1
#         else:
#             print("Computer wins this round!")
#             computer_score += 1
#
#         print(f"Score -> You: {player_score}, Computer: {computer_score}")
#         print("-----")
#
#     if player_score == 5:
#         print("🎉 Congratulations! You won the match!")
#     else:
#         print("💻 Computer wins the match! Better luck next time!")
# play_game()
















