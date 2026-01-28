word = input("Enter a word: ")
palindrome = word[::-1]
if word == palindrome:
    print("this is a palindrome")
else:
    print("this is not a palindrome")