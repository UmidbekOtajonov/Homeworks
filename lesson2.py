# boolean1
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username != "" and password != "":
#     print("True")
# else:
#     print("False")
#
# boolean 2
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a == b:
#     print("Numbers are equal")
# else:
#     print("Numbers are not equal")
#
# boolean3
#
# a = int(input("Enter a :"))
# if a >= 0 and a % 2 == 0:
#     print("True")
# else:
#     print("False")
#
# boolean4
#
# a = float(input("Enter a :"))
# b = float(input("Enter b :"))
# c = float(input("Enter c :"))
# if a != b and a !=c:
#     print("True")
# else:
#     print("False")
#
# boolean5
#
# word1 = input("Enter  string: ")
# word2 = input("Enter  string: ")
# if len(word1) == len(word2):
#     print("True")
# else:
# #     print("False")
#
# boolean6
#
# a  = int(input("Enter a number: "))
# if a % 3 == 0 and a % 5 == 0:
#     print("True")
# else:
#     print("False")
# #
#
# boolean7
#
# num1 = float(input("Birinchi sonni kiriting: "))
# num2 = float(input("Ikkinchi sonni kiriting: "))
# if 10<= num1 <= 20 and 10<= num2 <= 20 and num1 + num2 > 50.8:
#     print("True")
# else:
#     print("False")
#
#
# String1
#
# from datetime import date
#
# name = input("Enter your name: ")
# birthyear = int(input("Enter your birthyear: "))
# age = date.today().year - birthyear
# print("Your age is:", age)
#
# String2
#
# txt = 'LMaasleitbtui'
# car_name = txt[::2]
# print(car_name)
#
# String3
#
# string = input('Enter a string: ')
# Len = len(string)
# Upper_string = string.upper()
# Lower_string = string.lower()
# print(Len)
# print(Upper_string)
# print(Lower_string)
#
# String 4
#
# word = input("Enter a word: ")
# palindrome = word[::-1]
# if word == palindrome:
#     print("this is a palindrome")
# else:
#     print("this is not a palindrome")
#
# String5
#
# words = input("enter a string :")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# vowel_count = 0
# consonant_count = 0
# for i in range(len(words)):
#     if words[i] in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1
# print("vowel_counts =" ,vowel_count, "consonant_counts =", consonant_count)
#
# String6
#
# word_1 = input("Enter a word: ")
# word_2 = input("Enter a word: ")
# if word_1 in word_2:
#     print(f" {word_1} in  {word_2}")
# elif word_2 in word_1:
#     print(f" {word_2} in  {word_1}")
# else:
#     print("word not contains another words")
#
# string7
#
# sentance = input("Enter a sentence: ")
# word = input("Enter a word: ")
# last_char =sentance.split(" ")[-1]
# print(last_char)
# new_sent = sentance.replace(last_char, word)
# print(new_sent)
#
# string8
#
# word = input('Enter a word: ')
# a = word[0]
# b = word[-1]
# print(f"first character = {a} , last character = {b} ")
#
#
# string9
#
# word = input("enter a word =")
# new_word = word[::-1]
# print("new word =",new_word)
#
# string10
#
# sentences = input("enter a sentence: ")
# new_sentences = sentences.replace(" ","")
# count = len(new_sentences)
# print("count =",count)
#
# string11
#
# word = input("Enter a word: ")
# print(word.isalpha())
#
# string12
#
# sentance = input("Enter a list of words: ")
# words = sentance.split()
# result = "-".join(words)
# print(result)
#
# string13
#
# word = input("Enter a string: ")
# result = word.split()
# print(result)
#
# string14
#
# a = input("Enter a: ")
# b = input("Enter b: ")
# print(a==b)
#
# string15
#
# text = input("Enter text: ")
# words = text.split()
# first_letters = [w[0] for w in words]
# new_word = "".join(first_letters)
# print(new_word)
#
# string16
#
# sentence = input("Enter a string: ")
# word = input("Enter a character: ")
# new_word = sentence.split(word)
# result = "".join(new_word)
# print(result)
#
# string17
#
# word = input("Enter a word: ")
# vowels = ['a', 'e', 'i', 'o', 'u']
#
# result = [ "*" if w in vowels else w for w in word ]
#
# print("".join(result))
#
#
# string18
#
# sentance = input("Enter a sentence: ")
# items = sentance.split(" ")
# if items[0] == items[-1]:
#     print("words are equal")
# else:
#     print("words are not equal")
#
# Number1
#
# a = float(input("Enter a number: "))
# print(f"{a:.2f}")
#
# Number2
#
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
# c = int(input("Enter c number: "))
# Max = max(a, b, c)
# Min = min(a, b, c)
# print(Max, Min)
#
# Number3
#
# kilometers = float(input("Enter kilometers number: "))
# print("meters =", 1000*kilometers)
# print("centimeters =", 100000*kilometers)
#
# Number4
#
# a = float(input("Enter a : "))
# b = float(input("Enter b : "))
# c = a//b
# d = a%b
# print(f"integer = {c}")
# print(f"remainder = {d}")
#
# Number5
#
# Temperature = float(input("enter celsius ="))
# Fahrenheit = (Temperature * 9/5) + 32
# print(f"Fahrenheit = {Fahrenheit}")
#
# Number6
#
# a = input("enter a =")
# print(a[-1])
#
# Number7
#
# a = int(input("Enter a number: "))
# if a%2 == 0:
#     print("Even")
# else:
#     print("Odd")